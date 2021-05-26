import flask
from flask import Flask
from flask import request
import uuid
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template('index.html')

@app.route("/translate", methods=['POST'])
def translate():
    data = json.loads(flask.request.data.decode("utf-8"))
    to_translate = data["to_translate"]
    language = data["language"]
    # Add your subscription key and endpoint
    subscription_key = "subscription_key"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "westus2"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [language]
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': to_translate
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))

