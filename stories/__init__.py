from action import Action
from user import User

from .self_worth import story as self_worth

DEFAULT_ACTIONS = {
    'Look Around the area': Action(
        name='Look Around the area'
    )
}

STORIES = {
    'self_worth': self_worth
}

for story in STORIES.values():
    for quest in story.quests.values():
        quest.actions.update(DEFAULT_ACTIONS)

def look(user: User):
    print(user.location.description)

