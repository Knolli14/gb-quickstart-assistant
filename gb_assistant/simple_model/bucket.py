from google.cloud import storage

def download_blob(bucket_name, source_blob_name):
    """Downloads a blob from the bucket."""
    #breakpoint()
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    game = blob.download_as_string()

    print(f"Blob {source_blob_name} downloaded")

    return game
