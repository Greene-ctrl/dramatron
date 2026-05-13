import argparse
import sys
import os

from ..core.generator import StoryGenerator
from ..core.llm import GoogleAPI, OpenAIAPI, GroqAPI
from ..core.prompts import PREFIXES

def main():
    parser = argparse.ArgumentParser(description="Dramatron Terminal CLI")
    parser.add_argument("--logline", type=str, help="The logline of the story")
    parser.add_argument("--prefix_set", type=str, default="medea_prefixes", choices=list(PREFIXES.keys()), help="The prefix set to use")
    parser.add_argument("--provider", type=str, default="google", choices=["google", "openai", "groq"], help="LLM provider")
    parser.add_argument("--api_key", type=str, help="API key for the provider")
    parser.add_argument("--model", type=str, help="Model name")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("DRAMATRON_API_KEY")
    if not api_key:
        print("Error: API key must be provided via --api_key or DRAMATRON_API_KEY environment variable.")
        sys.exit(1)

    logline = args.logline
    if not logline:
        logline = input("Enter the logline: ")

    prefixes = PREFIXES[args.prefix_set]

    if args.provider == "google":
        client = GoogleAPI(api_key=api_key, sample_length=511, model=args.model or "gemini-1.5-pro")
    elif args.provider == "openai":
        client = OpenAIAPI(api_key=api_key, sample_length=511, model=args.model or "gpt-4-1106-preview")
    elif args.provider == "groq":
        client = GroqAPI(api_key=api_key, sample_length=511, model=args.model or "mixtral-8x7b-32768")

    generator = StoryGenerator(storyline=logline, prefixes=prefixes, client=client, verbose=True)

    # Run steps and handle failures
    steps = [
        (0, "Title"),
        (1, "Characters"),
        (2, "Scenes"),
        (3, "Places"),
        (4, "Dialogs")
    ]

    for level, name in steps:
        success = generator.step(level)
        if not success:
            print(f"\nFATAL ERROR: Failed to generate {name}. Aborting.")
            sys.exit(1)

    print("\n--- Final Script ---")
    story = generator.get_story()
    # Simple rendering for CLI
    print(f"TITLE: {story.title}")
    print("\nCHARACTERS:")
    for name, desc in story.character_descriptions.items():
        print(f"{name}: {desc}")

    print("\nSCRIPT:")
    for i, scene in enumerate(story.scenes.scenes):
        print(f"\nINT/EXT. {scene.place}")
        if scene.place in story.place_descriptions:
            print(story.place_descriptions[scene.place].description)
        print(f"\n{scene.plot_element}: {scene.beat}")
        if i < len(story.dialogs):
            print("\nDIALOG:")
            print(story.dialogs[i])

if __name__ == "__main__":
    main()
