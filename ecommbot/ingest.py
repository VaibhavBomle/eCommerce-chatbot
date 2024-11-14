from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
from ecommbot.data_convert import dataconverter
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# API KEYS
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN =os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

# loading embedding models
#embedding_google = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=GEMINI_API_KEY)
embedding_openai = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

# ingest data in AstraDB
def ingestdata(status):
    vstore = AstraDBVectorStore(
        embedding=embedding_openai,
        collection_name="chatbotecomm",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        TOKEN=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )

    storage = status

    if storage == None:
        docs = dataconverter()
        inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    return vstore, inserted_ids

if __name__ == "__main__":
    vstore,inserted_ids = ingestdata(None)
    print(f"Inserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell me the sound basshead")
    for res in results:
        print(f"* {res.page_content [{res.metadata}]}")
