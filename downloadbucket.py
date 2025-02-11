import os
import subprocess
from google.cloud import storage
import pandas as pd

# Configurações
PROJECT_ID = "seu-projeto"
SERVICE_NAME = "meu-servico"
REGION = "us-central1"
BUCKET_NAME = "meu-bucket"
IMAGE_NAME = f"gcr.io/{PROJECT_ID}/{SERVICE_NAME}:latest"
CSV_FILE = "arquivo.csv"

# Função para fazer deploy no Google Cloud Run
def deploy_cloud_run():
    print("Construindo a imagem Docker...")
    subprocess.run(["docker", "build", "-t", IMAGE_NAME, "."], check=True)
    
    print("Fazendo push da imagem para o GCR...")
    subprocess.run(["gcloud", "auth", "configure-docker", "--quiet"], check=True)
    subprocess.run(["docker", "push", IMAGE_NAME], check=True)
    
    print("Implantando no Cloud Run...")
    subprocess.run([
        "gcloud", "run", "deploy", SERVICE_NAME,
        "--image", IMAGE_NAME,
        "--platform", "managed",
        "--region", REGION,
        "--allow-unauthenticated"
    ], check=True)
    print("Deploy concluído!")

# Função para criar um bucket
def create_bucket():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    bucket.create(location=REGION)
    print(f"Bucket {BUCKET_NAME} criado!")

# Função para fazer upload de um arquivo
def upload_file():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(CSV_FILE)
    blob.upload_from_filename(CSV_FILE)
    print(f"{CSV_FILE} enviado para {BUCKET_NAME}.")

# Função para fazer download do arquivo
def download_file():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(CSV_FILE)
    blob.download_to_filename(f"baixado_{CSV_FILE}")
    print(f"{CSV_FILE} baixado como baixado_{CSV_FILE}.")

# Função para listar arquivos no bucket
def list_files():
    client = storage.Client()
    blobs = client.list_blobs(BUCKET_NAME)
    print("Arquivos no bucket:")
    for blob in blobs:
        print(blob.name)

# Função para ler e exibir um CSV
def read_csv():
    df = pd.read_csv(CSV_FILE)
    print("Dados do CSV:")
    print(df.head())

if __name__ == "__main__":
    # Exemplo de uso
    # deploy_cloud_run()
    # create_bucket()
    # upload_file()
    # download_file()
    # list_files()
    # read_csv()
    pass
