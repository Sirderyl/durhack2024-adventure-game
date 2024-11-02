from location import Location
from quest import Quest

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
        self.introduction = introduction
        self.starting_location = starting_location
        self.character_name = character_name
        self.character_description = character_description

        self.locations = {location.id: location for location in locations}
        self.quests = {quest.id: quest for quest in quests}
