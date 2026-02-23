import json
import os

FILENAME = "shopping.json"

def load_list():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)