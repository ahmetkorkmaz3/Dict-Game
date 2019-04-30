from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)

app_id = "de9425de"
app_key = "a9606bfd23d2e9fef2d545c6264cb64d"
language = "en"
words = ["strong", "example", "snow", "car", "table"]
correct_words = ["affect", "software", "engineer", "camel", "week"]
synonyms_words = {}

sentences = []

for word in words:
    """
    sentence_url = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/" + word + "/sentences"
    r = requests.get(sentence_url, headers={
        "app_id": app_id,
        "app_key": app_key
    })

    temp = r.json()
    sentence = temp['results'][0]['lexicalEntries'][0]['sentences'][0]['text']
    sentence = sentence.replace(word, "_______")
    sentences.append(sentence)

    print(sentences)
    """
    synonyms_url = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/synonyms"
    s = requests.get(synonyms_url, headers={
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
        "X-RapidAPI-Key": "c3261220b5msh244ebdbd879c92ap1708e1jsnb383e654e8a1"
    })
    temp2 = s.json()
    synonyms_words[word] = temp2['synonyms'][0]

#print(synonyms_words)
#sentence=sentences[question_id],

@app.route('/question/<int:question_id>', methods=['POST', 'GET'])
def question(question_id):
    if request.method == 'POST':
        result = request.form
        return result
    else:
        return render_template('question.html', correct_word=correct_words[question_id], synonym=synonyms_words)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
