from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__)

app_id = "9e47702d"
app_key = "7ae2304d9e92db2b1b01ca9128ac6eba"
language = "en"
words = ["strong", "example", "snow", "car", "table"]
correct_words = ["affect", "software", "engineer", "camel", "week"]
synonyms_words = {}

sentences = []

for word in words:
    sentence_url = "https://od-api.oxforddictionaries.com/api/v2/entries/en/" + word
    r = requests.get(sentence_url, headers={
        "app_id": app_id,
        "app_key": app_key,
    })
    temp = r.json()
    sentence = temp['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['examples'][0]['text']
    sentence = sentence.replace(word, "_______")
    sentences.append(sentence)

    synonyms_url = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/synonyms"
    s = requests.get(synonyms_url, headers={
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
        "X-RapidAPI-Key": "c3261220b5msh244ebdbd879c92ap1708e1jsnb383e654e8a1"
    })
    temp2 = s.json()
    synonyms_words[word] = temp2['synonyms'][0]


@app.route('/')
def index():
    return render_template('index.html', questions=sentences, words=words, synonyms=synonyms_words, correct_words=correct_words)

if __name__ == "__main__":
    app.run(debug = True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
