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
    query = """insert into users (username, first_name, last_name, email, password)
    values(?,?,?,?,?)"""
    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()

def delete_user (conn, username):
    query = f"Select * FROM users WHERE username = {username}"
    cursor = conn.cursor()
    cursor.execute(query,(username,))
    data = list(cursor.execute(query))
    
def edit_user (conn, username, details):
    query = f"Select {details} FROM users WHERE username = {username}"
    cursor = conn.cursor()