from flask import Flask, render_template, url_for
import requests
import json

app_id = "9e47702d"
app_key = "7ae2304d9e92db2b1b01ca9128ac6eba"
language = "en"
word = "example"
api_url = "https://od-api.oxforddictionaries.com/api/v2/entries/en/" + word
url = "https://od-api.oxforddictionaries.com/api/v1/entries/en/example/sentences"
r = requests.get(api_url, headers={"app_id": app_id, "app_key": app_key,})

json = r.json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', json=json)
