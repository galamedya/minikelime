import sqlite3

def create_connection():
    conn = sqlite3.connect("telegram_bot.db")
    return conn

def init_db():
    conn = create_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        is_admin INTEGER
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY
    )
    """)

    conn.commit()
    conn.close()

init_db()
