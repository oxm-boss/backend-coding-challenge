from flask import Flask, jsonify
from backend_coding_challenge import  get_languages_data

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def index():
    return """
        <p>
            Available Endpoints: <br />
            <strong style="margin-left:3em;">/fetch:</strong>
            <span style="margin-left:5em;">return a json object which list all languages with repositories</span>
        </p>
        """

@app.route("/fetch")
def fetch():
    languages = get_languages_data()
    return jsonify(languages)

