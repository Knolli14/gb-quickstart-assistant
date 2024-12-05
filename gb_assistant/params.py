import os
import json

# Google Cloud Storage
GC_BUCKET_NAME = os.environ.get("GC_BUCKET_NAME")

# Path to chromadb collections
STORE_PATH = "./store"

GAMES_LIST = [file.strip(".pdf") for file in os.listdir("raw_data")]

with open("games.json", "w") as f:
    f.write(json.dumps(GAMES_LIST))
