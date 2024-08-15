#!/usr/bin/env python3
"flask app"
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    "home route"
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user():
    "home route"
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    # Port should be an integer, not a string
    app.run(host="0.0.0.0", port=5000)
