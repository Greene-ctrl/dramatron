import unittest
from dramatron.core.models import Title, Character, Characters, Scene, Scenes, extract_elements, END_MARKER, TITLE_ELEMENT
from dramatron.core.generator import StoryGenerator
from dramatron.core.llm import LanguageAPI, LanguageResponse
from dramatron.core.prompts import MEDEA_PREFIXES

class MockLanguageAPI(LanguageAPI):
    def sample(self, prompt, sample_length=None, seed=None, num_samples=1):
        # Return different responses based on the prompt content
        if "Title:" in prompt:
            return [LanguageResponse(text="Mock Title**END**", text_length=10, prompt=prompt, prompt_length=len(prompt))]
        if "CHARACTERS_PROMPT" in prompt or "**Character:**" in prompt:
            return [LanguageResponse(text="**Character:** MockChar **Description:** A mock character.**END**", text_length=20, prompt=prompt, prompt_length=len(prompt))]
        if "SCENE_PROMPT" in prompt or "**Scenes:**" in prompt:
            return [LanguageResponse(text="Place: MockPlace\nPlot element: MockPlot\nBeat: MockBeat\n**END**", text_length=20, prompt=prompt, prompt_length=len(prompt))]
        if "SETTING_PROMPT" in prompt:
            return [LanguageResponse(text="Description: A mock description.**END**", text_length=20, prompt=prompt, prompt_length=len(prompt))]
        if "DIALOG_PROMPT" in prompt:
            return [LanguageResponse(text="Mock Dialog**END**", text_length=10, prompt=prompt, prompt_length=len(prompt))]
        return [LanguageResponse(text="Mock Response**END**", text_length=13, prompt=prompt, prompt_length=len(prompt))]

class TestCore(unittest.TestCase):
    def test_extract_elements(self):
        text = "Title: My Story**END**"
        elements = extract_elements(text, TITLE_ELEMENT, END_MARKER)
        self.assertEqual(elements, ["My Story"])

    def test_title_from_string(self):
        text = "Title: The Brave Rabbit**END**"
        title = Title.from_string(text)
        self.assertEqual(title.title, "The Brave Rabbit")

    def test_character_from_string(self):
        text = "Rabbit**Description:** A brave rabbit."
        char = Character.from_string(text)
        self.assertEqual(char.name, "Rabbit")
        self.assertEqual(char.description, "A brave rabbit.")

    def test_characters_from_string(self):
        text = "**Character:** Rabbit **Description:** A brave rabbit. \n**Character:** Fox **Description:** A cunning fox. \n"
        chars = Characters.from_string(text)
        self.assertEqual(len(chars.character_descriptions), 2)
        self.assertEqual(chars.character_descriptions["Rabbit"], "A brave rabbit.")
        self.assertEqual(chars.character_descriptions["Fox"], "A cunning fox.")

    def test_full_generation_pipeline(self):
        client = MockLanguageAPI(sample_length=511)
        generator = StoryGenerator(storyline="A mock story.", prefixes=MEDEA_PREFIXES, client=client, verbose=False)

        self.assertTrue(generator.step(0)) # Title
        self.assertEqual(generator.title, "Mock Title")

        self.assertTrue(generator.step(1)) # Characters
        self.assertIn("MockChar", generator.characters.character_descriptions)

        self.assertTrue(generator.step(2)) # Scenes
        self.assertEqual(len(generator.scenes.scenes), 1)

        self.assertTrue(generator.step(3)) # Places
        self.assertIn("MockPlace.", generator.places)

        self.assertTrue(generator.step(4)) # Dialogs
        self.assertEqual(len(generator.dialogs), 1)

        story = generator.get_story()
        self.assertEqual(story.title, "Mock Title")

if __name__ == "__main__":
    unittest.main()
