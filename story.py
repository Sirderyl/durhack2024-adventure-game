class Story:
    def __init__(
            self,
            title: str,
            description: str,
            # TODO: Pass location object
            starting_location: str,
            character_name: str,
            character_description: str
    ):
        self.title = title
        self.description = description
        self.starting_location = starting_location
        self.character_name = character_name
        self.character_description = character_description
