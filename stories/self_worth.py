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

throw_meat = Action(
    name="Throw a piece of raw meat",
    response="""
        As Lira edges closer to the fox blocking her path, she feels her nerves buzzing with urgency. The fox’s 
        golden eyes glint with a cunning that seems to pierce right through her, a sly grin curling at the 
        edges of his muzzle.

        “Well?” he sneers. “Still think you can make it past me? You’re hardly worth a second glance.”

        Lira clenches her jaw, fighting the urge to argue, and instead lets her hand drift to her pouch, her 
        fingers brushing against a scrap of raw meat she packed earlier for her journey.

        Her mind races. Maybe… just maybe this will work.

        She keeps her movements slow and deliberate, careful not to draw the fox’s attention. Then, with a 
        swift, practiced motion, she pulls out the meat and flings it far off into the shadows, the faint scent 
        of it filling the damp air.

        The fox’s nose twitches, his mocking expression flickering with sudden interest. His gaze snaps toward 
        the meat, his body tensing as instinct takes hold.

        Without a second thought, he bolts toward the meat, his tail flashing like a streak of fire through 
        the mist as he darts into the underbrush.

        Lira doesn’t wait to see what he does next. She steps lightly around where he’d been lounging, feeling 
        her pulse quicken as she hurries down the newly opened path. Behind her, the fox is muttering, somewhere 
        off in the shadows.

        “Crafty little wanderer,” he calls out begrudgingly, his voice growing faint. “Perhaps there’s more to you 
        than I thought.”

        A hint of satisfaction blooms in Lira’s chest as she presses onward, the mist closing around her once more. 
        She knows the fox won’t be far behind, but for now, she’s free to continue her journey.
    """
)

agree_with_mirror = Action(
    name="Agree with the mirror"
)

ignore_mirror = Action(
    name="Ignore the mirror",
    response="""
        But as she stares into the false future, something deep within her stirs, a small flicker of defiance. 
        She thinks of Brannor’s words, of the journeyman’s hammer he gave her, a symbol of the strength she’s 
        forged through countless days of hard work and resilience.

        With a trembling hand, she reaches into her pouch and pulls out the hammer. Its solid weight grounds her, 
        bringing clarity back into her mind. Gritting her teeth, she meets the gaze of her hollow-eyed reflection 
        and whispers fiercely, "This isn’t me. And this isn’t my future."

        As her resolve strengthens, the glass shivers, cracks splintering across its surface. Her reflection 
        distorts, the despairing image warping and fading as light breaks through the cracks. With a final, 
        resounding snap, the mirror shatters, shards scattering across the path, disappearing into the mist.

        Lira stands taller, the weight lifting from her shoulders. She’s still uncertain of the road ahead, 
        but a fire has rekindled within her, stronger than the shadows and false visions meant to hold her back. 
        And so, she moves forward, more determined than ever.
    """
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
    actions=[throw_rock, throw_meat],
    important_action=throw_meat
)

facing_the_mirror = Quest(
    id="facing_the_mirror",
    title="Facing the Mirror",
    description="""
        
        Lira continues down the mist-laden path, her breath steadying after her encounter with the fox. But as she 
        rounds a bend, she freezes. There, half-hidden in the shadows, stands an ornate mirror framed in twisted 
        silver vines. The glass shimmers with an eerie, dark light, drawing her closer despite a sense of dread 
        crawling up her spine.

        She hesitates, but something compels her to step forward, her gaze locking onto the glass. In it, 
        she sees herself—but this reflection is different, wrong somehow. The mirror shows her standing alone, 
        her hands empty and trembling. The crown is nowhere to be seen.

        And then, the scene shifts. She sees faces—familiar faces from her village—watching her with cold, 
        distant eyes. Her mentor Brannor turns away, a flicker of disappointment crossing his face, as if he, too, 
        has given up on her. Other villagers shake their heads, their whispers reaching her like ghostly echoes:

        "She was never meant for this."

        "How foolish to think she was strong enough."

        Her reflection slumps, eyes hollow, her spirit crushed. The weight of failure seeps into her bones, 
        and a whisper from the glass chills her to the core: This is your fate. This is all you’ll ever be—a 
        disappointment, a shadow forgotten by all.

        A wave of despair crashes over her, her knees weakening as her heart sinks. The idea of turning back, 
        of abandoning the quest, begins to seem almost... reasonable. The path forward feels impossibly heavy, 
        and her spirit trembles on the edge of breaking.
    """,
    actions=[ignore_mirror, agree_with_mirror],
    important_action=ignore_mirror
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

    locations=[ravenwood, vale_of_shadows],
    quests=[journey_begins, meeting_the_fox, facing_the_mirror]
)
