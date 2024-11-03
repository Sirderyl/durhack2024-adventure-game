#!/usr/bin/env python3

from flask import Flask, Response, request
from flask_cors import CORS
from stories import STORIES, DEFAULT_ACTIONS
from typing import Any
import llm_action_mapping as lam

import json

class JsonEncoder(json.JSONEncoder):
    def default(self, o: Any):
        return o.__dict__
encoder = JsonEncoder()

app = Flask(__name__)
CORS(app)

@app.route('/stories')
def stories():
    return Response(json.dumps(list(STORIES.keys())), mimetype='application/json')

@app.route('/story/<id>')
def story(id: str):
    story = STORIES[id]
    return Response(encoder.encode(story), mimetype='application/json')

@app.route('/response')
def response():
    story = request.args.get('story')
    if story is None:
        return Response('Missing story parameter', status=400)
    story = STORIES[story]

    quest = request.args.get('quest')
    if quest is None:
        return Response('Missing quest parameter', status=400)
    quest = story.quests[quest]

    location = request.args.get('location')
    if location is None:
        return Response('Missing location parameter', status=400)
    location = story.locations[location]

    player_input = request.args.get('input')
    if player_input is None:
        return Response('Missing input parameter', status=400)

    predicted_action = lam.predict_action(player_input, quest.actions)
    if predicted_action == "invalid action":
        return Response(json.dumps({
            'outcome': "Invalid action"
        }), mimetype='application/json')

    action_obj = quest.actions[predicted_action]
    if action_obj.response is None:
        outcome = lam.generate_outcome(
            action_obj,
            quest.actions,
            quest,
            location
        )
    else:
        outcome = action_obj.response

    return Response(json.dumps({
        'action': predicted_action,
        'outcome': outcome
    }), mimetype='application/json')

app.run(port=5000)
