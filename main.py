#!/usr/bin/env python3

from flask import Flask, Response
from stories import STORIES
from typing import Any

import json

class JsonEncoder(json.JSONEncoder):
    def default(self, o: Any):
        return o.__dict__
encoder = JsonEncoder()

app = Flask(__name__)

@app.route('/story/<id>')
def story(id: str):
    story = STORIES[id]
    return Response(encoder.encode(story), mimetype='application/json')

app.run(port=5000)
