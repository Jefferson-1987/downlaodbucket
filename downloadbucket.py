# import packages
from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/Windows/OneDrive/Documentos/bucket/agendaporangatu-e859ed36b9b1.json'

# define function that downloads a file from the bucket
def download_cs_file(bucket_name, file_name, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)
    blob.download_to_filename(destination_file_name)

    return True

download_cs_file('dashporangatu', 'agendaporangatu.csv', 'agendalocal.csv')