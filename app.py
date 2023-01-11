import os

import openai
from flask import Flask, redirect, render_template, request, url_for
import json

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

def generate_prompt_text(text):
    return text
    
@app.route('/generate_completion', methods=['POST'])
def welcome():
    input_json = request.get_json(force=True) 
    prompt_text = input_json['prompt']

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt_text(prompt_text),
        temperature=0.6,
    )
    gpt_response = response['choices'][0]['text']
    dict_text = {"text": gpt_response}
    result = {"messages": [dict_text]}
    print(result)

    return json.dumps(result, ensure_ascii=False)
