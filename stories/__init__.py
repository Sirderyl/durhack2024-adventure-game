from action import Action
from user import User

from .self_worth import story as self_worth

STORIES = {
    'self_worth': self_worth
}

def look(user: User):
    print(user.location.description)

DEFAULT_ACTIONS = {
    'Look Around the area': Action(
        name='Look Around the area'
    )
}
