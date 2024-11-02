from inspect import cleandoc

from location import Location
from quest import Quest

def header(char: str, for_text: str):
    longest_line = max(for_text.split("\n"), key=len)


    return char * len(longest_line)

def with_header(before: str, after: str, text: str):
    return f"{header(before, text)}\n{text}\n{header(after, text)}"

class Story:
    def __init__(
            self,
            title: str,
            introduction: str,
            starting_location: Location,
            character_name: str,
            character_description: str,

            locations: list[Location],

            quests: list[Quest],
    ):
        self.title = title
        self.introduction = cleandoc(introduction)
        self.starting_location = starting_location
        self.character_name = character_name
        self.character_description = cleandoc(character_description)

        self.locations = {location.id: location for location in locations}
        self.quests = {quest.id: quest for quest in quests}

    def print_intro(self):
        print(with_header("=", "=", self.title))

        print(with_header("", "-", self.introduction))

        print(with_header("", "-", self.character_description))
