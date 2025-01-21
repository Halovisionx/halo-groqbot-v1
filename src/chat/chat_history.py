# src/chat/chat_history.py
import pandas as pd
from sqlalchemy.orm import Session
from src.db import get_db

def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY, role TEXT, content TEXT)''')
    conn.commit()
    conn.close()

def save_message(role, content):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()



def load_messages():
    conn = next(get_db())
    df = pd.read_sql_query("SELECT * FROM messages", conn)
    return df
