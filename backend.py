from flask import Flask
import json
import os

app = Flask(__name__)

print(os.getcwd())


@app.route('/')
def home():
    return "go to api"

@app.route('/repo')
def repo():
    
    return repositories

@app.route('/related/<tech1>/<tech2>')
def related(tech1, tech2):
    print(tech1, tech2)
    return repositories

import pickle
@app.route('/api/')
def api():

    
    with open('index.json', 'r') as f:
        index = json.load(f)
        keys = list(index.keys())
        print(type(keys))
        # print(keys)

    with open('matrix.json', 'r') as f:
        matrix = json.load(f)

    api = {"matrix": matrix, "keys": keys}
    return json.dumps(api)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")