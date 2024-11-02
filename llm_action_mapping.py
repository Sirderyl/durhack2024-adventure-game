import google.generativeai as genai
from story_vars import story_desc, start_location, quest1_desc, get_story

story = get_story("self_worth")

# Define valid actions per scene
valid_actions = story.quests["journey_begins"].actions

api_key = "AIzaSyBWFVhLGTuaVqhmsTajxaZNqNK58XNYDCI"

# Example function to create a structured prompt
def create_prompt(player_input, valid_actions):
    prompt = (
        f"Player input: '{player_input}'\n\n"
        "Determine if the input corresponds to any of these valid actions:\n"
        f"{', '.join(valid_actions)}\n\n"
        "If the input matches, return the closest action name. "
        "If no valid action is matched, return 'invalid action'."
    )
    return prompt

def create_response_prompt(action, scene):
    if scene == "forge" and action == "look around":
        prompt = (
            f"{story_desc}\n\n"
            f"{start_location}\n\n"
            f"{quest1_desc}\n\n"
            "Player chose this action: '{action}'\n\n"
            "Provide a very short description of the player's surroundings, highlighting "
            "that the blacksmith is waiting for the player to talk to them."
        )
    else:
        prompt = (
        f"Player chose this action in a text-based adventure game: '{action}'\n\n"
        "Provide a response to the player's action."
    )
    
    return prompt

def get_llm_response(player_input, scene):
    prompt = create_prompt(player_input, valid_actions[scene])

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    action = response.text.strip()
    
    for valid_action in valid_actions[scene]:
        if valid_action in action:
            print(valid_action)
            return valid_action

    return "invalid action"


def llm_action(action, scene):
    prompt = create_response_prompt(action, scene)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def perform_action(player_input, scene):
    action = get_llm_response(player_input, scene)
    response = ""
    if action == "invalid action":
        response = "Invalid action. Please try again."
    else:
        print(f"Performing action: {action}")
        response = llm_action(action, scene)
    
    print(response)

#perform_action("I want to observe my surroundings", "forge")
print(valid_actions[1].__getattribute__("name"))