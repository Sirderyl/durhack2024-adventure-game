from action import Action
from story import Story
from location import Location
from quest import Quest
from user import User

def speak_blacksmith_result(user: User):
    pass # TODO: Implement

speak_blacksmith = Action(
    name="Talk to blacksmith",
    response="""
        A conversation between Lira and the blacksmith Brannor:

        Brannor: "Lira, word’s come from the king’s court." 

        Lira: (frowns) "More news of the crown, I suppose. They say it’s broken beyond repair."

        Brannor: "Aye, that’s the talk. The kingdom is restless, and they need someone who can find it, 
        someone who can mend it." (He pauses, looking at her with a thoughtful glint in his eye.)

        Lira: (shakes her head) "And what has that got to do with me? I’m just an apprentice. 
        I’m not… I’m not anything special, Master Brannor."

        Brannor: (smiling gently) "Oh, aren’t you now? Funny, because I’ve yet to see anyone as 
        stubborn with an anvil as you. You work as if every strike counts, as if it’s life itself." 
        (He steps closer, his voice softening.) "That spark in you, Lira—that’s more precious than you know. 
        It’s a fire that the Vale cannot snuff out."

        Lira: (looking away) "But the Vale… they say it twists people. I don’t know if I’m strong 
        enough. What if I can’t… if I can’t bring the crown back?"

        Brannor: (placing a steady hand on her shoulder) "Strength isn’t in knowing you’ll succeed, 
        child. It’s in facing what frightens you, despite the doubt." (He reaches into a leather satchel 
        beside him and pulls out a small hammer, its handle worn and comfortable-looking, with runes 
        carefully etched into the metal.)

        Lira: (eyes widening) "Is that… the Journeyman’s Hammer? The one you always kept on the top shelf?"

        Brannor: "Aye. Carved it myself back in my younger days. It’s a simple tool, but solid. 
        Just like you, Lira. It won’t break easily, and neither will you. Take it, and let it remind 
        you of the strength you’ve already built."

        Lira: (holds the hammer, feeling its weight in her hands, finding a strange comfort in it) 
        "But… I don’t know if I’m ready. What if I fail?"

        Brannor: (gruffly, but kindly) "Then you’ll learn, as we all do. Even the finest blade gets 
        forged in fire, struck over and over till it’s strong enough to cut true. Remember, there’s no 
        shame in falling, so long as you rise again."

        Lira: (taking a deep breath, she nods) "Alright, Master Brannor. I’ll go. I don’t know what 
        I’ll find, but… I’ll go."

        Brannor: (smiling, a warmth in his voice) "That’s my girl. Trust yourself. And if you find that 
        fox lurking in the Vale, well…" (he winks) "give him a reason to respect a Ravenwood blacksmith."

        (As Lira leaves, she looks back to see Brannor watching her, pride and quiet hope in his eyes. 
        She grips the hammer, feeling a surge of courage as she steps into the unknown.)
    """
)

throw_rock = Action(
    name="Throw a rock"
)

ravenwood = Location(
    id="ravenwood",
    name="Ravenwood Forge",
    description="""
        You are in a forge inside a small medieval village surrounded by a
        dense forest, called Ravenwood. Ravenwood is known for its skilled blacksmiths and woodworkers.
    """
)

vale_of_shadows = Location(
    id="vale_of_shadows",
    name="The Vale of Shadows",
    description="""
        You are in The Vale of Shadows, a place where the air is always misty,
        and the sun rarely shines through. This place is known for testing the
        courage and hearts of those who wander here.
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

meeting_the_fox = Quest(
    id="meeting_the_fox",
    title="Meeting the Fox",
    description="""
        As Lira ventures deeper into the thick mist of the Vale of Shadows, a flicker of movement catches 
        her eye. Out of the shadows steps a sleek, amber-colored fox with eyes sharp as daggers. He sits 
        squarely in her path, his tail swishing with amusement.

        “Well, well,” he sneers, his voice a mocking drawl. “Another lost soul, thinking she can mend 
        what’s already broken. The crown is beyond the reach of one as small as you.”

        Lira feels a pang of doubt but steadies herself. She tries to step around him, but the fox 
        sidesteps, blocking her again. He tilts his head, studying her with a gleam of mischief.

        “Going somewhere, are we?” he purrs. “I don’t think so, you're big enough disappointment already.”

        Lira is hit with a wave of self-doubt. She can feel the fox’s words burrowing into her heart,
        but she knows she must press on. She must find a way to outwit the fox and continue her quest.
    """,
    actions=[],
    important_action=None
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
