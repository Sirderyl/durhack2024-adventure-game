from typing import Callable, Type

# Avoid circular imports
User = Type["User"]

def always_true(_):
    return True

class Action:
    def __init__(
        self,
        name: str,
        # Condition that must be met for the action to be available
        check: Callable[[User], bool] = always_true,
    ):
        self.name = name
        self.check = check
