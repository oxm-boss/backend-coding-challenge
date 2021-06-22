from flask import Flask, jsonify
from backend_coding_challenge import  get_languages_data

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def index():
    return "Hello World!"

@app.route("/fetch")
def fetch():
    languages = get_languages_data()
    return jsonify(languages)

