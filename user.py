from story import Story
from typing import Optional

class User:
    def __init__(
            self,
            token: Optional[int],
            story: Story,
            location: str, # TODO: Resolve to object
            active_quest: Optional[str], # TODO: Resolve to object
            completed_quests: list[str] # TODO: Resolve to object
    ):
        self.token = token
        self.story = story
        self.location = location
        self.active_quest = active_quest
        self.completed_quests = completed_quests
