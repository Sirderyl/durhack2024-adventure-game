import google.generativeai as genai
# from story_vars import story_desc, start_location, quest1_desc, get_story

from action import Action
from location import Location
from quest import Quest
from stories import STORIES, DEFAULT_ACTIONS

# This shouldn't be hardcoded. Too bad.
api_key = "AIzaSyBWFVhLGTuaVqhmsTajxaZNqNK58XNYDCI"

# Example function to create a structured prompt
def create_prompt(player_input, valid_actions: dict[str, Action]):
    action_names = [action.name for action in valid_actions.values()]

    prompt = (
        "This is a text-based adventure game. The player is in a scene and can perform actions.\n\n"
        "Pick the action that most closely matches the player's input.\n\n"
        "Return the name of your choice as it appeared in the input and nothing else.\n\n"
        "If there are no good matches, return 'invalid action'.\n\n"
        "Your valid actions are:\n"
        f"{'\t'.join(action_names)}\n\n"
        "The player's input is:\n"
        f"{player_input}\n\n"
    )
    return prompt

def create_response_prompt(action: Action, available_actions: dict[str, Action], location: Location, quest: Quest):
    action_names = [action.name for action in available_actions.values()]
    prompt = (
        "This is a text-based adventure game. The player's current quest is:\n\n"
        f"{quest.description}\n\n"
        "The player's current location is:\n\n"
        f"{location.description}\n\n"
        f"Describe the player performing the action '{action.name}' in the context of the quest and location.\n\n"
        "Provide a 1-2 sentence description, followed by a sentence describing what could happen next.\n\n"
        f"{'\t'.join(action_names)}\n\n"

    )

    return prompt

def get_llm_response(player_input, valid_actions: dict[str, Action]):
    prompt = create_prompt(player_input, valid_actions)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def llm_action(action: Action, available_actions: dict[str, Action], quest, location):
    prompt = create_response_prompt(action, available_actions, quest, location)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def perform_action(player_input: str, quest: Quest, location: Location, available_actions: dict[str, Action]):
    action = get_llm_response(player_input, available_actions)
    response = ""
    if action == "invalid action":
        response = "Invalid action. Please try again."
    else:
        print(f"Performing action: {action}")
        action = available_actions[action]
        if action.response is None:
            response = llm_action(action, available_actions, quest, location)
        else:
            response = action.response

    print(response)

story = STORIES['self_worth']
quest = story.quests['journey_begins']

actions = DEFAULT_ACTIONS.copy()
actions.update(quest.actions)

perform_action("I want to observe my surroundings", quest, story.starting_location, actions)
