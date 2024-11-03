from action import Action
from story import Story
from location import Location
from quest import Quest
from user import User


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

discourage_bard = Action(
    name="Agree with bard's negativity"
)

bard_negativity = Action(
    name="Bard's negativity brings Lira down"
)

encourage_bard = Action(
    name="Give the bard words of encouragement",
    response="""
        Lira studies him, her heart aching at his words. She knows too well the weight of self-doubt, 
        the sting of feeling unseen. “You know, I was told something recently,” she says, her voice gentle. 
        “That strength isn’t in knowing you’ll succeed but in trying despite the doubt. Maybe… maybe the worth 
        of your music isn’t in whether others listen, but in how it makes you feel.”

        The bard looks at her, surprise flickering in his eyes.

        “Play because you love it,” Lira urges. “Play because it’s a part of you. Music has its own kind of magic, 
        one that doesn’t need an audience to be real.”

        The bard hesitates, then slowly lifts the lute again. He plucks a few strings, and the familiar melody 
        spills into the air, tentative at first but growing stronger with each note. His eyes close as he lets 
        himself sink into the music, his fingers dancing along the strings, playing with a quiet, heartfelt passion 
        that seems to fill the grove.

        Lira sits beside him, letting the music wash over her, feeling its warmth and joy. For the first 
        time in a long while, the bard smiles, his face lighting up as he plays not for an audience, but for himself.

        When he finishes, he looks at her, his cheeks flushed. “Thank you, Lira. I… I’d forgotten what that felt like.”

        She smiles, giving him an encouraging nod. “Remember that feeling. Let it guide you.”

        As she rises to leave, the bard presses a small charm into her hand—a token of gratitude. 
        “Take this, for luck,” he says shyly. “A little melody to carry with you on your quest.”

        With a final smile, she bids him farewell, her spirit buoyed by the magic of his music and the 
        reminder that true worth comes from within.
    """
)

do_not_fix_crown = Action(
    name="Attempt to quit and not fix the crown"
)

fix_crown = Action(
    name="Decide to fix the crown",
    response="""
        “If it means saving the kingdom,” she says quietly, “then I accept. Let them remember the crown, 
        the peace it brings… that’s enough.”

        A faint smile touches the mage’s lips, a hint of admiration in his eyes. “Very well, child.”

        He extends his hand, and a silver light flows from his fingertips, enveloping the crown. Lira watches 
        in awe as the shattered jewels mend, their color blazing to life, and the dull metal gleams once more. 
        When the light fades, the crown is whole—a symbol of unity and strength, gleaming with restored glory.

        Lira’s heart swells, pride and sorrow mingling as she looks upon her work, knowing it will never be 
        hers to claim. She rises, the weight of her decision settling in, but with it, a sense of peace she hadn’t 
        expected.

        The mage nods approvingly. “Your sacrifice will not be in vain, Lira of Ravenwood. You have proven that 
        true worth lies not in fame, but in the heart’s quiet strength.”

        With that, he vanishes, leaving Lira alone in the glade. She carefully lifts the crown, feeling its warmth, 
        and turns to carry it back to the kingdom, her spirit renewed, her heart steady.
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

the_sad_bard = Quest(
    id="the_sad_bard",
    title="The Sad Bard",
    description="""
        As Lira steps past the shattered remnants of the mirror, the mist around her begins to clear slightly, 
        and the faint sound of soft, mournful music drifts through the air. She follows the melody, 
        her heart drawn to its melancholy beauty, until she finds herself in a small grove where a young man 
        sits on a moss-covered rock, his head bowed over a lute.

        The bard’s fingers hover uncertainly over the strings, his eyes cast downward. His clothes are worn, 
        and his expression is one of quiet defeat. He doesn’t notice Lira at first, lost in his own world as he 
        strums a gentle tune, each note quivering with sadness.

        Lira approaches him slowly, careful not to startle him. “That’s a beautiful song,” she says softly.

        The bard jumps, nearly dropping his lute. He looks up, his face coloring with embarrassment. 
        “Oh! I didn’t… I didn’t think anyone was listening,” he mutters, eyes flicking away. 
        “I’m just… practicing. It’s nothing special.”

        Lira sits beside him, glancing at the lute. “It sounded special to me. Why do you play, if I may ask?”

        The bard shrugs, his gaze drifting back to his instrument. “I used to play for others in my village, 
        but… they stopped listening. No one really cared for my music.” He sighs, his fingers tracing the 
        strings absently. “Sometimes I wonder if there’s any point in playing at all.”
    """,
    actions=[discourage_bard, bard_negativity, encourage_bard],
    important_action=encourage_bard
)

finding_the_crown = Quest(
    id="finding_the_crown",
    title="Finding the Crown",
    description="""
        As Lira steps into a hidden glade, her breath catches. There, nestled among the roots of an ancient tree, 
        lies the broken crown. Its once-glorious metal is tarnished, the jewels cracked and dull, a symbol of 
        power now fallen into ruin. She kneels beside it, reaching out with trembling hands, and grasps her hammer, 
        feeling the weight of her journey pressing down on her.

        With a steadying breath, she raises the hammer, striking the crown gently, trying to reshape it, 
        to breathe life back into its metal and jewels. But as she hammers, nothing happens—the crown remains 
        stubbornly fractured, resisting her efforts.

        A wave of frustration and exhaustion wells up within her. After all this… have I come this far only to 
        fail? Her shoulders slump, doubt creeping back into her heart.

        Just as her spirit begins to falter, a soft glow fills the glade. She looks up to see a figure standing 
        at the edge of the clearing, shrouded in a cloak of shimmering blue. It’s an old mage, his eyes sharp and 
        filled with ancient wisdom. He steps forward, his gaze fixed on the broken crown.

        “Child,” he says in a voice that seems to echo through time, “you’ve come farther than most. But the magic 
        you need to restore the crown is beyond mere tools or brute strength. It requires a sacrifice.”

        Lira’s heart races, hope mingling with apprehension. “You mean… you can help me fix it?”

        The mage nods, a slight smile playing at his lips. “I can, but only if you’re willing to pay the price.” 
        His gaze is piercing, and she feels as if he’s looking into the very core of her soul. “If I lend you my 
        magic, none shall know of your courage. No songs will be sung in your honor, no tales will be told. The 
        kingdom will be saved, but your name will be lost to history, your deeds hidden in shadow.”

        Lira’s heart pounds, the weight of the choice pressing down on her. She had dreamt of proving herself, of 
        being seen as someone worthy, someone brave. And now, when she’s finally on the brink of restoring the crown, 
        she’s asked to relinquish all recognition.

        The mage’s gaze remains steady, unyielding. “Consider this carefully, Lira. Some heroes wear their glory; 
        others carry it silently, their deeds known only to themselves.”

        For a long moment, Lira is silent, wrestling with her pride, her doubts, and her heart’s truest desires. 
        Finally, she lifts her head, her eyes resolute.
    """,
    actions=[do_not_fix_crown, fix_crown],
    important_action=fix_crown
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
    quests=[journey_begins, meeting_the_fox, facing_the_mirror, the_sad_bard, finding_the_crown]
)
