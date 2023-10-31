import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import logging
import time

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        print("Azure Blob Storage Python quickstart sample")
        account_url = os.getenv("ACCOUNT_URL")
        cred = os.getenv("CLIENT_ID")
        credential=DefaultAzureCredential(managed_identity_client_id = cred) 

        # Create the BlobServiceClient object
        while(True):
            blob_service_client = BlobServiceClient(account_url, credential=credential)
            container_name = str(uuid.uuid4())
            container_client = blob_service_client.create_container(container_name)
            print("Storage container created")
            time.sleep(10)
            blob_service_client.delete_container(container_name)
            print("Storage container deleted")
            blob_service_client.close()
    except Exception as e:
        logging.exception("Unable to connect to storage client"+ e)
        return func.HttpResponse(
            "Cannot connect to storage client",
            status_code=500
        )


    return func.HttpResponse(
             "Successfully connected to storage client",
             status_code=200
        )
