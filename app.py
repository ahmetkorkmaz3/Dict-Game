from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__)

app_id = "9e47702d"
app_key = "7ae2304d9e92db2b1b01ca9128ac6eba"
language = "en"
words = ["strong","example", "snow", "car", "pencil", "table"]
sentences = []

for word in words:
    api_url = "https://od-api.oxforddictionaries.com/api/v2/entries/en/" + word
    r = requests.get(api_url, headers={"app_id": app_id, "app_key": app_key,})
    temp = r.json()
    sentence = temp['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['examples'][0]['text']
    sentence = sentence.replace(word, "_______")
    sentences.append(sentence)

print(sentences)

@app.route('/')
def index():
    return render_template('index.html', questions=sentences, words=words)

if __name__ == "__main__":
    app.run(debug = True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
