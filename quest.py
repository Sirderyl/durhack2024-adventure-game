from inspect import cleandoc

class Quest:
    def __init__(
        self,
        id: str,
        description: str,
    ):
        self.id = id
        self.description = cleandoc(description)
