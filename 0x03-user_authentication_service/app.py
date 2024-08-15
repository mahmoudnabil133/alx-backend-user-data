#!/usr/bin/env python3
"flask app"
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    "home route"
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    # Port should be an integer, not a string
    app.run(host="0.0.0.0", port=5000)
