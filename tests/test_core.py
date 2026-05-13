import unittest
from dramatron.core.models import Title, Character, Characters, Scene, Scenes, extract_elements, END_MARKER, TITLE_ELEMENT

class TestModels(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
