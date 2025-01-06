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
