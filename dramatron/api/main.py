from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Dict, Optional
import os

from ..core.generator import StoryGenerator
from ..core.llm import GoogleAPI, OpenAIAPI, GroqAPI
from ..core.prompts import PREFIXES

app = FastAPI(title="Dramatron API")

class GenerationRequest(BaseModel):
    logline: str
    prefix_set: str = "medea_prefixes"
    model_provider: str = "google" # google, openai, groq
    api_key: str
    model_name: Optional[str] = None

class StoryResponse(BaseModel):
    title: str
    characters: Dict[str, str]
    scenes: List[Dict[str, str]]
    place_descriptions: Dict[str, str]
    dialogs: List[str]

@app.post("/generate", response_model=StoryResponse)
async def generate_story(request: GenerationRequest):
    if request.prefix_set not in PREFIXES:
        raise HTTPException(status_code=400, detail="Invalid prefix set")

    prefixes = PREFIXES[request.prefix_set]

    if request.model_provider == "google":
        client = GoogleAPI(api_key=request.api_key, sample_length=511, model=request.model_name or "gemini-1.5-pro")
    elif request.model_provider == "openai":
        client = OpenAIAPI(api_key=request.api_key, sample_length=511, model=request.model_name or "gpt-4-1106-preview")
    elif request.model_provider == "groq":
        client = GroqAPI(api_key=request.api_key, sample_length=511, model=request.model_name or "mixtral-8x7b-32768")
    else:
        raise HTTPException(status_code=400, detail="Invalid model provider")

    generator = StoryGenerator(storyline=request.logline, prefixes=prefixes, client=client, verbose=False)

    # Hierarchical generation with explicit step tracking
    steps = [
        (0, "Title"),
        (1, "Characters"),
        (2, "Scenes"),
        (3, "Places"),
        (4, "Dialogs")
    ]

    for level, name in steps:
        try:
            success = generator.step(level)
            if not success:
                raise HTTPException(status_code=500, detail=f"Generation failed at step: {name}")
        except Exception as e:
            if isinstance(e, HTTPException): raise e
            raise HTTPException(status_code=500, detail=f"Error generating {name}: {str(e)}")

    story = generator.get_story()

    return {
        "title": story.title,
        "characters": story.character_descriptions,
        "scenes": [{"place": s.place, "plot_element": s.plot_element, "beat": s.beat} for s in story.scenes.scenes],
        "place_descriptions": {name: p.description for name, p in story.place_descriptions.items()},
        "dialogs": story.dialogs
    }

@app.get("/prefixes")
async def get_prefixes():
    return list(PREFIXES.keys())
