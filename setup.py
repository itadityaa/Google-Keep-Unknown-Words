import os
import logging

def create_directories():
    directories = [
        "data",
        "src",
        "tests"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("Directories created:", directories)

def create_files():
    files = {
        "data/note.txt": "Add your exported Google Keep note here.",
        "src/__init__.py": "",
        "src/main.py": "# Entry point of the project",
        "src/word_extractor.py": """\
import re

def extract_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = re.findall(r'\\b\\w+\\b', text)
    return [word.lower() for word in words]
""",
        "src/dictionary_api.py": """\
import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def fetch_meaning(word):
    response = requests.get(f"{API_URL}{word}")
    if response.status_code == 200:
        data = response.json()
        return "; ".join([f"{m['partOfSpeech']}: {d['definition']}" 
                          for m in data[0]['meanings'] 
                          for d in m['definitions']])
    return "Meaning not found"
""",
        "src/database_manager.py": """\
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
""",
        "src/config.py": """\
NOTE_PATH = "data/note.txt"
DB_PATH = "data/word_meanings.db"
""",
        "src/logger.py": """\
import logging

def get_logger(name, log_file='app.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    return logger
""",
        "tests/test_word_extractor.py": "# Tests for word_extractor.py",
        "tests/test_dictionary_api.py": "# Tests for dictionary_api.py",
        "tests/test_database_manager.py": "# Tests for database_manager.py",
        "tests/test_end_to_end.py": "# Tests for end-to-end functionality",
        ".gitignore": "*.db\n*.pyc\n__pycache__/",
        "README.md": "# Word Meaning Project\n\nThis project retrieves meanings of words from a Google Keep note and stores them in an SQL database.",
        "requirements.txt": "requests"
    }

    for file_path, content in files.items():
        with open(file_path, "w") as file:
            file.write(content)
    print("Files created:", list(files.keys()))

if __name__ == "__main__":
    print("Setting up the project structure...")
    create_directories()
    create_files()
