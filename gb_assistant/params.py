import os

LOCAL_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "raw_data"
)

GAME_NAME = "7 wonders duel"

GC_BUCKET_NAME = os.environ.get("GC_BUCKET_NAME")

STORE_PATH = "./store"

LLAMA_CLOUD_API_KEY = os.environ.get("LLAMA_CLOUD_API_KEY")
#>>>>>>> b05efc596f3ef17e62ceca1c375a218c6d05b67d
