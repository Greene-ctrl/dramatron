from typing import Dict, List, NamedTuple, Optional, Union
import collections

# ------------------------------------------------------------------------------
# Script markers
# ------------------------------------------------------------------------------

END_MARKER = '**END**'
STOP_MARKER = '\n'
CHARACTER_MARKER = '**Character:** '
DESCRIPTION_MARKER = '**Description:** '
SCENES_MARKER = '**Scenes:**'
DIALOG_MARKER = '**Dialog:**'
LOGLINE_MARKER = "**Logline:** "
TITLE_ELEMENT = 'Title: '
CHARACTERS_ELEMENT = 'Characters: '
DESCRIPTION_ELEMENT = 'Description: '
PLACE_ELEMENT = 'Place: '
PLOT_ELEMENT = 'Plot element: '
PREVIOUS_ELEMENT = 'Previous beat: '
SUMMARY_ELEMENT = 'Summary: '
BEAT_ELEMENT = 'Beat: '
LOGLINE_ELEMENT = "Logline: "

# ------------------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------------------

def extract_elements(text: str, begin: str, end: str) -> List[str]:
    """Extracts elements from a text string given string and ending markers."""
    results = []
    start = 0
    while True:
        start = text.find(begin, start)
        if start == -1:
            return results
        # Look for the ending marker AFTER the beginning marker
        finish = text.find(end, start + len(begin))
        if finish == -1:
            return results
        results.append(text[start + len(begin):finish].strip())
        start = finish + len(end)

def strip_remove_end(text: str) -> str:
    text = text.strip()
    end_marker_stripped = END_MARKER.strip()
    if text.endswith(end_marker_stripped):
        text = text[:-len(end_marker_stripped)]
    return text

# ------------------------------------------------------------------------------
# Dramatron script entities
# ------------------------------------------------------------------------------

class Title(NamedTuple):
    """Title class."""
    title: str

    @classmethod
    def from_string(cls, text: str):
        title_list = extract_elements(text, TITLE_ELEMENT, END_MARKER)
        title = title_list[0] if title_list else ""
        return cls(title)

    def to_string(self):
        s = ''
        s += TITLE_ELEMENT + self.title
        s += END_MARKER
        return s

class Character(NamedTuple):
    """Character class."""
    name: str
    description: str

    @classmethod
    def from_string(cls, text: str):
        elements = text.split(DESCRIPTION_MARKER)
        if len(elements) == 2:
            name = elements[0].strip()
            description = elements[1].strip()
            return cls(name, description)
        else:
            return None

class Characters(NamedTuple):
    """Characters class, containing main characters and their descriptions."""
    character_descriptions: Dict[str, str]

    @classmethod
    def from_string(cls, text: str):
        """Parses the characters from the generated text."""
        text = text.strip()
        character_descriptions = {}
        # Ensure text ends with STOP_MARKER for extract_elements to work
        if not text.endswith(STOP_MARKER):
            text += STOP_MARKER
        elements = extract_elements(text, CHARACTER_MARKER, STOP_MARKER)
        for text_character in elements:
            character = Character.from_string(text_character)
            if character is not None:
                character_descriptions[character.name] = character.description
        return cls(character_descriptions)

    def to_string(self):
        s = '\n'
        for name, description in self.character_descriptions.items():
            s += '\n' + CHARACTER_MARKER + ' ' + name + ' ' + DESCRIPTION_MARKER + ' '
            s += description + ' ' + STOP_MARKER + '\n'
        s += END_MARKER
        return s

class Scene(NamedTuple):
    """Scene class."""
    place: str
    plot_element: str
    beat: str

    def to_string(self):
        s = PLACE_ELEMENT + ' ' + self.place + '\n'
        s += PLOT_ELEMENT + ' ' + self.plot_element + '\n'
        s += BEAT_ELEMENT + ' ' + self.beat + '\n'
        return s

class Place(NamedTuple):
    """Place class."""
    name: str
    description: str

    @classmethod
    def format_name(cls, name: str):
        if name.find('.') == -1:
            name = name + '.'
        return name

    @classmethod
    def from_string(cls, place_name: str, place_text: str):
        place_text += END_MARKER
        description = extract_elements(place_text, DESCRIPTION_ELEMENT, END_MARKER)
        desc = description[0] if description else ""
        return cls(place_name, desc)

    @classmethod
    def format_prefix(cls, name):
        s = PLACE_ELEMENT + name + '\n' + DESCRIPTION_ELEMENT
        return s

    def to_string(self):
        s = self.format_prefix(self.name) + self.description + '\n\n'
        return s

class Scenes(NamedTuple):
    """Scenes class."""
    scenes: List[Scene]

    @classmethod
    def from_string(cls, text: str):
        """Parse scenes from generated scenes_text."""
        places = extract_elements(text, PLACE_ELEMENT, PLOT_ELEMENT)
        plot_elements = extract_elements(text, PLOT_ELEMENT, BEAT_ELEMENT)
        beats = extract_elements(text, BEAT_ELEMENT, '\n')

        num_complete_scenes = min([len(places), len(plot_elements), len(beats)])
        scenes = []
        for i in range(num_complete_scenes):
            scenes.append(
                Scene(Place.format_name(places[i]), plot_elements[i], beats[i]))
        return cls(scenes)

    def to_string(self):
        s = ''
        for scene in self.scenes:
            s += '\n' + scene.to_string()
        s += END_MARKER
        return s

    def num_places(self):
        return len(set([scene.place for scene in self.scenes]))

    def num_scenes(self) -> int:
        return len(self.scenes)

class Story(NamedTuple):
    """Story class."""
    storyline: str
    title: str
    character_descriptions: Dict[str, str]
    place_descriptions: Dict[str, Place]
    scenes: Scenes
    dialogs: List[str]
