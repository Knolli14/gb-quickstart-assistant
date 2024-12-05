from google.cloud import storage
from gb_assistant import params
import os

def download_blob(bucket_name, source_blob_name):
    """Downloads a blob from the bucket."""

    json_key_path = os.path.join(os.path.dirname(__file__), 'service-account.json')
    storage_client = storage.Client.from_service_account_json(json_key_path)
    #storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    game = blob.download_as_string()


    return game

