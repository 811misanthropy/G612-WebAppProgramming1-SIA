

from flask import Flask, request
from flask_cors import CORS

from repository.py 

app = Flask("MyFirstUserManagerApp")
CORS(app)

DB_FILE = ""

@app.route('/api/v1/users', methods=["POST"])
def users():
    user_details = request.json
    try:
        conn = get_connection(DB_FILE)
        create_user(conn, user_details)
        conn.close()
        return '', 200
    except Exception as e:
        error = {

        }

@app.route('/api/v1/users/<email>', methods=["GET"])
def get_user(email):
    if email is None:
        error = {
            "error" : "--Invalid email."
        }
        return error, 400

    try:
        conn = get_connection(DB_FILE)
        users = get_email_and_password(conn, email)
        r


@app.route('/api/v1/sign-in', methods=["POST"])
def sign_in():
    body = request.json
    email = body.get("email", None)
    password = body.get("password", None)
    if email is None:
        error = {
            "error": ""
        }
    if password is None:
        error = {
            "error": ""
        }
    
    #sign in
    try:
        conn = get_connection(DB_FILE)
        user = get_email_and_password(conn, email)
        if user and user[1] == password:
            return '', 204
        else:
            error = {
                "error": "--failed to sign-in. Email or password are invalid"
            }
            
    except Exception as e:
        error = {
            "error": f"--Failed to sign-in. {e}"
        }


if __name__ == "__main__":
    app.run(port=3002, debug=True)