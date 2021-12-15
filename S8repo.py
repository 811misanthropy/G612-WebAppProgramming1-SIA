import sqlite3
from sqlite3.dbapi2 import Cursor

def connect(dbfile):
    conn = sqlite3.connect('users.db')
    return conn

def get_users(conn):
    query = "Select * from users"
    cursor = conn.cursor()
    data = list(cursor.execute(query))
    return data

def get_user_by_username(conn, username):
    query = f"SELECT username, password, FROM users WHERE username = {username}"
    cursor = conn.cursor()
    results = list(cursor.execute(query))
    return results[0]

def create_user(conn, user_data):
    query = """insert into users (id, username, first_name, last_name, email, password, created_at)
    values(?,?,?,?,?,?,?)"""
    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()
    cursor.close()

# delete
def delete_user(conn, user_id=None, username=None):
    query = ""
    if user_id is not None:
        query = f"delete from users where id = {user_id}"
    if username is not None:
        query = f"delete from users where username = '{username}'"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


# update
def update_user(conn, user_id=None, username=None, details=None):
    """
    UPDATE table_name
    SET column1 = value1, column2 = value2...., columnN = valueN
    WHERE [condition];

    details = {
    "email": "a@c.com"
    }
    """
    set_statement = ""
    for key, value in details.items():
        set_statement = set_statement + f"{key}={value},"
    set_statement = set_statement[:-1]
    query = ''
    if user_id is not None:
        query = f"update users set {set_statement} where id = {user_id}"
    if username is not None:
        query = f"update users set {set_statement} where username = '{username}'"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()