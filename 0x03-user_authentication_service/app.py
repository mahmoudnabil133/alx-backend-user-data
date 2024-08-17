#!/usr/bin/env python3
"flask app"
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    "home route"
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_users():
    """Route to register a new user"""
    data = request.form
    email = data.get('email')
    password = data.get('password')

    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    "login"
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie('session_id', session_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    "logout"
    try:
        sess_id = request.cookies.get('session_id')
        user = AUTH.get_user_from_session_id(sess_id)
        AUTH.destroy_session(user.id)
        return redirect(url_for('home'))
    except Exception as e:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    "get user profile if logged in"
    sess_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sess_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def profile():
    "get reset token with post req"
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except Exception:
        abort(403)


if __name__ == "__main__":
    # Port should be an integer, not a string
    app.run(host="0.0.0.0", port=5000)
