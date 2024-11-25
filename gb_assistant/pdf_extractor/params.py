import os

URL = os.environ.get("URL")

LOCAL_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "raw_data"
)
