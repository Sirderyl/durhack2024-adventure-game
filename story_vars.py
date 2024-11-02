from stories import STORIES

def get_story(story_name):
    return STORIES[story_name]

story = get_story("self_worth")

story_desc = "This is a text-based adventure game. Story description: Player plays as " + story.character_description

start_location = story.locations["ravenwood"].description

quest1_desc = story.quests["journey_begins"].description