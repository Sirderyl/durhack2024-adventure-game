from typing import Callable

def always_true(_):
    return True

class Action:
    def __init__(
        self,
        name: str,
        #result: Callable[..., None],
        # Condition that must be met for the action to be available
        check: Callable[..., bool] = always_true,
    ):
        self.name = name
        #self.result = result
        self.check = check
