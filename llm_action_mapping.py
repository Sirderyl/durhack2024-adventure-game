import os
import google.generativeai as genai
from strip_markdown import strip_markdown

from action import Action
from location import Location
from quest import Quest


api_key = os.getenv("GEMINI_API_KEY")


# Example function to create a structured prompt
def create_prompt(player_input: str, valid_actions: dict[str, Action]):
    action_names = [action.name for action in valid_actions.values()]

    prompt = (
        "This is a text-based adventure game. The player is in a scene and can perform actions.\n\n"
        "Pick the action that most closely matches the player's input.\n\n"
        "Return the name of your choice as it appeared in the input and nothing else.\n\n"
        "If there are no good matches, return 'invalid action'.\n\n"
        "Your valid actions are:\n"
        f"{''.join(action_names)}\n\n"
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
        f"Make sure to include next needed action of {quest.important_action.name}, but don't draw too much attention to it.\n\n"
        f"{''.join(action_names)}\n\n"
    )

    return prompt

def predict_action(player_input: str, valid_actions: dict[str, Action]):
    prompt = create_prompt(player_input, valid_actions)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def generate_outcome(action: Action, available_actions: dict[str, Action], quest: Quest, location: Location):
    prompt = create_response_prompt(action, available_actions, location, quest)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    text = response.text.strip()
    return strip_markdown(text)

if __name__ == "__main__":
    from stories import STORIES
    s = STORIES["self_worth"]

    print(generate_outcome(
        s.quests["journey_begins"].actions['Look Around the area'],
        s.quests["journey_begins"].actions,
        s.quests["journey_begins"],
        s.starting_location
    ))
