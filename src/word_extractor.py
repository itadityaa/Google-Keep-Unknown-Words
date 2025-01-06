import re

def extract_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text)
    return [word.lower() for word in words]
