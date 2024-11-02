from typing import Optional

from story import Story
from location import Location
from quest import Quest

class User:
    def __init__(
            self,
            token: Optional[int],
            story: Story,
            location: Location,
            active_quest: Optional[Quest],
            completed_quests: list[Quest]
    ):
        self.token = token
        self.story = story
        self.location = location
        self.active_quest = active_quest
        self.completed_quests = completed_quests
