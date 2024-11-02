from inspect import cleandoc

class Quest:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
    ):
        self.id = id
        self.title = title
        self.description = cleandoc(description)
