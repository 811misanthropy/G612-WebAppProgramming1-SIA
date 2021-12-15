import sqlite3

def get_connection (dbfile):
        try:
            conn = sqlite3.connect(dbfile)
            return conn
        except Exception as e:
            raise   e

def get_username_and_password (conn, email=None):
    querry =""
    try:
        cursor = conn.cursor()
        user = list(cursor.execute(querry))
        if len(user[0]):
            user=user[0]
        return user
    except Exception as e:
        raise e