import os
from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):
    if not os.path.exists(destination_file_name):
        """Downloads a blob from the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_name)

        print(f'Blob {source_blob_name} downloaded to {destination_file_name}.')
