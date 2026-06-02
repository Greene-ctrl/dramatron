import collections
import time
from typing import Dict, List, Optional, Tuple, Any

from .models import (
    BEAT_ELEMENT, CHARACTER_MARKER, CHARACTERS_ELEMENT, DESCRIPTION_ELEMENT,
    DIALOG_MARKER, END_MARKER, PLACE_ELEMENT, PLOT_ELEMENT, PREVIOUS_ELEMENT,
    SCENES_MARKER, STOP_MARKER, SUMMARY_ELEMENT, TITLE_ELEMENT,
    Character, Characters, Place, Scene, Scenes, Story, Title,
    extract_elements, strip_remove_end
)
from .llm import LanguageAPI, FilterAPI, LanguageResponse

# Hyperparameters (defaults)
DEFAULT_SEED = 1
SAMPLING_PROB = 0.95
SAMPLING_TEMP = 1.0
SAMPLE_LENGTH_TITLE = 64
SAMPLE_LENGTH_PLACE = 128
SAMPLE_LENGTH = 511
MAX_PARAGRAPH_LENGTH_CHARACTERS = 1024
MAX_PARAGRAPH_LENGTH_SCENES = 1024
MAX_PARAGRAPH_LENGTH = 1024
MAX_RETRIES = 10
MAX_NUM_REPETITIONS = 3
MAX_NUM_ATTEMPTS_GET_OUT_OF_LOOP = 3

def detect_loop(text: str, max_num_repetitions: int = MAX_NUM_REPETITIONS):
    """Detect loops in generated text."""
    blocks = text.split('\n\n')
    num_unique_blocks = collections.Counter(blocks)
    for block in blocks:
        num_repetitions = num_unique_blocks[block]
        if num_repetitions > max_num_repetitions:
            return True
    return False

def generate_text(generation_prompt: str,
                  client: LanguageAPI,
                  filter: Optional[FilterAPI] = None,
                  sample_length: Optional[int] = None,
                  max_paragraph_length: int = MAX_PARAGRAPH_LENGTH,
                  seed: Optional[int] = None,
                  num_samples: int = 1,
                  max_num_repetitions: Optional[int] = None) -> str:
    """Generate text using the generation prompt."""

    if sample_length is None:
        sample_length = client.default_sample_length
    max_num_calls = int(max_paragraph_length / sample_length) + 1
    num_calls = 0

    result = ''
    while True:
        prompt = generation_prompt + result
        success, current_seed = False, seed or 1
        retry_count = 0
        while success is False and retry_count < MAX_RETRIES:
            responses = client.sample(
                prompt=prompt,
                sample_length=sample_length,
                seed=current_seed,
                num_samples=num_samples)
            response = responses[0]

            # If the response is empty or indicates an error, retry with different seed
            if not response.text or response.text.startswith("Error") or response.text.startswith("Content blocked"):
                retry_count += 1
                current_seed += 1
                continue

            if filter is not None and not filter.validate(response.text):
                return 'Content was filtered out.' + END_MARKER

            if max_num_repetitions:
                success = not detect_loop(
                    response.text, max_num_repetitions=max_num_repetitions)
                if not success:
                    current_seed += 1
                    if current_seed > ((seed or 1) + MAX_NUM_ATTEMPTS_GET_OUT_OF_LOOP):
                        success = True
                    else:
                        retry_count += 1
                        continue
            else:
                success = True

        if not response.text:
            return result + END_MARKER # Give up after retries

        result = result + response.text
        num_calls += 1

        index = result.find(END_MARKER)
        if index != -1:
            return result[:index] + END_MARKER

        index = result.find('Example ')
        if index != -1:
            return result[:index] + END_MARKER

        if max_paragraph_length is not None and len(result) > max_paragraph_length:
            return result + END_MARKER
        if num_calls >= max_num_calls:
            return result + END_MARKER

    return result

def generate_text_no_loop(generation_prompt: str,
                          client: LanguageAPI,
                          filter: Optional[FilterAPI] = None,
                          sample_length: Optional[int] = None,
                          max_paragraph_length: int = MAX_PARAGRAPH_LENGTH,
                          seed: Optional[int] = None,
                          num_samples: int = 1) -> str:
    """Generate text using the generation prompt, without any loop."""
    return generate_text(
        generation_prompt=generation_prompt,
        client=client,
        filter=filter,
        sample_length=sample_length,
        max_paragraph_length=sample_length,
        seed=seed,
        max_num_repetitions=None,
        num_samples=num_samples)

def generate_title(storyline: str,
                   prefixes: Dict[str, str],
                   client: LanguageAPI,
                   filter: Optional[FilterAPI] = None,
                   seed: Optional[int] = None,
                   num_samples: int = 1):
    titles_prefix = prefixes['TITLES_PROMPT'] + storyline + ' ' + TITLE_ELEMENT
    title_text = generate_text_no_loop(
        generation_prompt=titles_prefix,
        client=client,
        filter=filter,
        sample_length=SAMPLE_LENGTH_TITLE,
        seed=seed,
        num_samples=num_samples)
    title = Title.from_string(TITLE_ELEMENT + title_text)
    return (title, titles_prefix)

def generate_characters(
    storyline: str,
    prefixes: Dict[str, str],
    client: LanguageAPI,
    filter: Optional[FilterAPI] = None,
    seed: Optional[int] = None,
    max_paragraph_length: int = MAX_PARAGRAPH_LENGTH_CHARACTERS,
    num_samples: int = 1):
    characters_prefix = prefixes['CHARACTERS_PROMPT'] + storyline
    characters_text = generate_text(
        generation_prompt=characters_prefix,
        client=client,
        filter=filter,
        seed=seed,
        max_paragraph_length=max_paragraph_length,
        num_samples=num_samples)
    characters = Characters.from_string(characters_text)
    return (characters, characters_prefix)

def generate_scenes(storyline: str,
                    character_descriptions: Dict[str, str],
                    prefixes: Dict[str, str],
                    client: LanguageAPI,
                    filter: Optional[FilterAPI] = None,
                    seed: Optional[int] = None,
                    max_paragraph_length: int = MAX_PARAGRAPH_LENGTH_SCENES,
                    num_samples: int = 1):
    scenes_prefix = prefixes['SCENE_PROMPT'] + storyline + '\n'
    for name in character_descriptions:
        scenes_prefix += character_descriptions[name] + '\n'
    scenes_prefix += '\n' + SCENES_MARKER
    scenes_text = generate_text(
        generation_prompt=scenes_prefix,
        client=client,
        filter=filter,
        seed=seed,
        max_paragraph_length=max_paragraph_length,
        num_samples=num_samples)
    scenes = Scenes.from_string(scenes_text)
    return (scenes, scenes_prefix)

def generate_place_descriptions(storyline: str,
                                scenes: Scenes,
                                prefixes: Dict[str, str],
                                client: LanguageAPI,
                                filter: Optional[FilterAPI] = None,
                                seed: Optional[int] = None,
                                num_samples: int = 1):
    place_descriptions = {}
    unique_place_names = set([scene.place for scene in scenes.scenes])
    place_prefix_base = prefixes['SETTING_PROMPT'] + storyline + '\n'
    place_prefixes = []
    for place_name in unique_place_names:
        place_suffix = Place.format_prefix(place_name)
        place_text = generate_text(
            generation_prompt=place_prefix_base + place_suffix,
            client=client,
            filter=filter,
            sample_length=SAMPLE_LENGTH_PLACE,
            seed=seed,
            num_samples=num_samples)
        place_text = place_suffix + place_text
        place_descriptions[place_name] = Place.from_string(place_name, place_text)
        place_prefixes.append(place_prefix_base + place_suffix)
    return (place_descriptions, place_prefixes)

def generate_dialog(storyline: str,
                    scenes: List[Scene],
                    character_descriptions: Dict[str, str],
                    place_descriptions: Dict[str, Place],
                    prefixes: Dict[str, str],
                    max_paragraph_length: int,
                    client: LanguageAPI,
                    filter: Optional[FilterAPI] = None,
                    max_num_repetitions: Optional[int] = None,
                    seed: Optional[int] = None,
                    num_samples: int = 1):
    scene = scenes[-1]
    place_t = PLACE_ELEMENT + scene.place + '\n'
    if scene.place in place_descriptions:
        place_description = place_descriptions[scene.place]
        if place_description:
            place_t += DESCRIPTION_ELEMENT + place_description.description
            place_t += '\n'

    characters_t = ''
    if character_descriptions:
        characters_t += CHARACTERS_ELEMENT
        for name in character_descriptions:
            if name in scene.beat:
                characters_t += character_descriptions[name] + '\n'

    plot_element_t = PLOT_ELEMENT + scene.plot_element + '\n'
    summary_t = SUMMARY_ELEMENT + storyline + '\n'
    if len(scenes) > 1:
        summary_t += PREVIOUS_ELEMENT + scenes[len(scenes) - 2].beat + '\n'
    beat_t = BEAT_ELEMENT + scene.beat + '\n'

    dialog_prefix = (
        prefixes['DIALOG_PROMPT'] + place_t + characters_t + plot_element_t +
        summary_t + beat_t)
    dialog_prefix += '\n' + DIALOG_MARKER + '\n'

    dialog = generate_text(
        generation_prompt=dialog_prefix,
        client=client,
        filter=filter,
        seed=seed,
        max_paragraph_length=max_paragraph_length,
        max_num_repetitions=max_num_repetitions,
        num_samples=num_samples)

    return (dialog, dialog_prefix)

class StoryGenerator:
    level_names = ('storyline', 'title', 'characters', 'scenes', 'places', 'dialogs')

    def __init__(
        self,
        storyline: str,
        prefixes: Dict[str, str],
        client: LanguageAPI,
        max_paragraph_length: int = 1024,
        max_paragraph_length_characters: int = MAX_PARAGRAPH_LENGTH_CHARACTERS,
        max_paragraph_length_scenes: int = MAX_PARAGRAPH_LENGTH_SCENES,
        num_samples: int = 1,
        filter: Optional[FilterAPI] = None,
        verbose: bool = True):
        self._prefixes = prefixes
        self._max_paragraph_length = max_paragraph_length
        self._max_paragraph_length_characters = max_paragraph_length_characters
        self._max_paragraph_length_scenes = max_paragraph_length_scenes
        self._num_samples = num_samples
        self._client = client
        self._filter = filter
        self._verbose = verbose

        self.prompts = {
            'title': '',
            'characters': '',
            'scenes': '',
            'places': {},
            'dialogs': []
        }
        self._title = Title('')
        self._characters = Characters({})
        self._scenes = Scenes([])
        self._places = {}
        self._dialogs = []

        self.interventions = {}
        self._level = 0
        self._set_storyline(storyline)

    def _log(self, message: str):
        if self._verbose:
            print(message)

    def _set_storyline(self, storyline: str):
        if storyline.find('.') == -1:
            storyline = storyline + '.'
        self._storyline = storyline
        timestamp = time.time()
        self.interventions[timestamp] = 'STORYLINE\n' + storyline

    @property
    def title(self) -> str:
        return self._title.title

    @property
    def characters(self) -> Characters:
        return self._characters

    @property
    def scenes(self) -> Scenes:
        return self._scenes

    @property
    def places(self) -> Dict[str, Place]:
        return self._places

    @property
    def dialogs(self) -> List[str]:
        return self._dialogs

    def step(self, level: Optional[int] = None, seed: Optional[int] = None, idx: Optional[int] = None) -> bool:
        if level is None:
            level = self._level
        level += 1
        self._level = level
        timestamp = time.time()
        self.interventions[timestamp] = f'STEP {level}\n'

        if level == 1:
            self._log("Generating Title...")
            title, prefix = generate_title(self._storyline, self._prefixes, self._client, self._filter, seed, self._num_samples)
            self._title = title
            self.prompts['title'] = prefix
            success = len(title.title) > 0
            if success: self._log(f"Title: {title.title}")
            return success

        if level == 2:
            self._log("Generating Characters...")
            chars, prefix = generate_characters(self._storyline, self._prefixes, self._client, self._filter, seed, self._max_paragraph_length_characters, self._num_samples)
            self._characters = chars
            self.prompts['characters'] = prefix
            success = len(chars.character_descriptions) > 0
            if success: self._log(f"Generated {len(chars.character_descriptions)} characters.")
            return success

        if level == 3:
            self._log("Generating Scenes...")
            scenes, prefix = generate_scenes(self._storyline, self._characters.character_descriptions, self._prefixes, self._client, self._filter, seed, self._max_paragraph_length_scenes, self._num_samples)
            self._scenes = scenes
            self.prompts['scenes'] = prefix
            success = len(scenes.scenes) > 0
            if success: self._log(f"Generated {len(scenes.scenes)} scenes.")
            return success

        if level == 4:
            self._log("Generating Place Descriptions...")
            places, prefixes = generate_place_descriptions(self._storyline, self._scenes, self._prefixes, self._client, self._filter, seed, self._num_samples)
            self._places = places
            self.prompts['places'] = {name: pre for name, pre in zip(places.keys(), prefixes)}
            success = len(places) > 0
            if success: self._log(f"Generated {len(places)} place descriptions.")
            return success

        if level == 5:
            self._log("Generating Dialogs...")
            if idx is None:
                dialogs = []
                dialog_prompts = []
                for k in range(len(self._scenes.scenes)):
                    self._log(f"  Generating Dialog for scene {k+1}...")
                    d, p = generate_dialog(self._storyline, self._scenes.scenes[:(k+1)], self._characters.character_descriptions, self._places, self._prefixes, self._max_paragraph_length, self._client, self._filter, MAX_NUM_REPETITIONS, seed, self._num_samples)
                    dialogs.append(d)
                    dialog_prompts.append(p)
                self._dialogs = dialogs
                self.prompts['dialogs'] = dialog_prompts
                return len(dialogs) > 0
            else:
                while len(self._dialogs) < len(self._scenes.scenes): self._dialogs.append('')
                while len(self.prompts['dialogs']) < len(self._scenes.scenes): self.prompts['dialogs'].append('')
                d, p = generate_dialog(self._storyline, self._scenes.scenes[:(idx+1)], self._characters.character_descriptions, self._places, self._prefixes, self._max_paragraph_length, self._client, self._filter, MAX_NUM_REPETITIONS, seed, self._num_samples)
                self._dialogs[idx] = d
                self.prompts['dialogs'][idx] = p
                return True
        return False

    def get_story(self) -> Story:
        return Story(
            storyline=self._storyline,
            title=self._title.title,
            character_descriptions=self._characters.character_descriptions,
            place_descriptions=self._places,
            scenes=self._scenes,
            dialogs=self._dialogs
        )
