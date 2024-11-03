from action import Action
from story import Story
from location import Location
from quest import Quest
from user import User

def speak_blacksmith_result(user: User):
    pass # TODO: Implement

speak_blacksmith = Action(
    name="Talk to blacksmith",
    response="# TODO: Something about talking to the blacksmith",
)

ravenwood = Location(
    id="ravenwood",
    name="Ravenwood Forge",
    description="""
        You are in a forge inside a small medieval village surrounded by a
        dense forest, called Ravenwood. Ravenwood is known for its skilled blacksmiths and woodworkers.
    """
)

journey_begins = Quest(
    id="journey_begins",
    title="The Journey Begins",
    description="""
        One day, a message arrives in Ravenwood with news that the kingdom's
        magical crown—the symbol of unity and strength—has been broken, and the
        spirit of the kingdom is weakening. The crown is rumored to be hidden in
        the Vale of Shadows, a place few return from. Lira is reluctant,
        doubting she has what it takes to find the crown and repair it.
        Lira’s mentor sees potential in her. He wants to speak with her.
    """,
    actions=[speak_blacksmith],
    important_action=speak_blacksmith
)

story = Story(
    title="The Broken Crown",
    introduction="""
        In the mystical land of Aeloria, a sprawling kingdom filled with vibrant
        villages, enchanted forests, and towering mountains, there is a hidden
        valley, The Vale of Shadows, where the air is always misty, and the sun
        rarely shines through. This place is known for testing the courage and
        hearts of those who wander there.
    """,

    starting_location=ravenwood,
    starting_quest=journey_begins,

    character_name="Lira",
    character_description="""
        Lira, a young, unassuming blacksmith's apprentice, has lived their life
        in the small village of Ravenwood. They are skilled with their hands,
        yet doubt their worth due to years of feeling overlooked and
        undervalued. Lira believes that they are destined to be an unknown
        apprentice forever, never to make a difference.
    """,

    locations=[ravenwood],
    quests=[journey_begins]
)
