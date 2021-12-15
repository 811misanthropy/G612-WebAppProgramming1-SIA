from logging import exception
from os import startfile
from types import resolve_bases
from flask import Flask
from flask import request
from werkzeug.wrappers import response


from S8repo import connect, get_users, get_user_by_username, create_user, delete_user, edit_user

app=Flask(__name__)

@app.route("/api/v1/users", methods=["GET","POST", "GETUN"])
def users():
    conn = connect("db/users.db")

    if request.method == "GET":
        users = get_users(conn)
        response = {
            'data': users
        }
        conn.close()
        return response, 200
  
    if request.method == "POST":
        user_data = request.json
        user_data = [
            user_data["id"],
            user_data["username"],
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["password"],
            user_data["created_at"],
            user_data["last_updated"],
            user_data["last_signed_in"]
        ]
        create_user(conn, user_data)

        conn.close()
        return '', 200

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        try: 
            conn=connect("db/users.db")
            data = get_users(conn)
            conn.close()
        except Exception as e:
            response = {}
            return response, 500
        for row in data:
            elememnts = {
                "id": None,
                "username": None,
                "first_name": None,
                "last_mail": None,
                "email": None
            }
        #response["users"].append(elememnts)
        #return response
            
@app.route("api/v1/changes", methods=["PUT"])
def users():

    if request.method == "PUT":
        conn = connect("db/users.db")
        users = get_users(conn)

@app.route('/api/<user_id>', methods=["PUT", "DELETE"])
def erase_user(user_id):
    if request.method == "DELETE":
        if not user_id or user_id == "null" or user_id == "undefined":
            response = {
                "error": "--Failed to delete user. Invalid user id provided; user_id = {user_id}"
            }
            return response, 400
            try:
                conn=connect("db/users.db")
                delete_user(conn, user_id=user_id)
                conn.close()
                return "", 200
            except Exception as e:
                response = {
                    "error": f"--Failed to delete user. Error {e}"
                }
                return response, 500
    

if __name__ == "__main__":
    app.run(port=5006, debug=True)


