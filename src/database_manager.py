import sqlite3

def initialize_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WordMeanings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE,
            meaning TEXT
        )
    ''')
    conn.commit()
    return conn

def insert_word(conn, word, meaning):
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO WordMeanings (word, meaning) VALUES (?, ?)', (word, meaning))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Word '{word}' already exists.")
