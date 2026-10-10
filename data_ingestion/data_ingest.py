from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv # importing dotenv variable
import os
import pandas as pd
from data_ingestion.data_transform import data_converter

load_dotenv()

ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT"),
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE"),
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

class ingest_data:
    def __init__(self):
        print("data ingestion has been init....")

    def data_ingestion(self):
        pass
