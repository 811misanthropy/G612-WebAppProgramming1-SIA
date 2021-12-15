from flask import Flask
from werkzeug.wrappers import request

from S8repo import connect, get_users, get_user_by_username, create_user, delete_user, edit_user

app=Flask(__name__)

@app.route("/api/v1/users", methods=["GET","POST"])
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

if __name__ == "__main__":
    app.run(port=5006, debug=True)

