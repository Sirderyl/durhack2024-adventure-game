from inspect import cleandoc
from action import Action

class Quest:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        actions: list[Action],
        important_action: Action,
    ):
        self.id = id
        self.title = title
        self.description = cleandoc(description)
        self.actions = {
            action.name: action
            for action in actions
        }
        self.important_action = important_action
