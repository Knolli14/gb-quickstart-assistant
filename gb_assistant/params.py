import os

LOCAL_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "raw_data"
)

LLAMA_CLOUD_API_KEY = os.environ.get("LLAMA_CLOUD_API_KEY")
