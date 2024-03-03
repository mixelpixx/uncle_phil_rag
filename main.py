import os
import shutil
from openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from IPython.display import Markdown, display
from llama_index.embeddings.openai import OpenAIEmbedding
import chromadb
import getpass
from flask import Flask, request, jsonify
import http.client
import json

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass.getpass("OpenAI API Key:")
openai.api_key = os.environ["OPENAI_API_KEY"]

chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

embed_model = OpenAIEmbedding(
    model="text-embedding-3-large",
    dimensions=512,
)

documents = SimpleDirectoryReader("./docs/").load_data()

if not documents:
    print("No documents found in the 'docs' folder. The database is empty.")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

def check_database_exists():
    return os.path.exists("./chroma_db")

def rebuild_database():
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )

def query_engine(user_message):
    engine = index.as_query_engine()
    query_results = engine.query(user_message)
    return query_results

def openai_chat(user_message, query_results):
    client = OpenAI()

    try:
        augmented_prompt = f"Answer the users question with info provided from db. Here is the relevant information from the database:\n{query_results}\nUser Query: {user_message}\nAnswer:"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[{"role": "system", "content": augmented_prompt}],  
            stream=True
        )

        final_response = ""
        for chunk in response:
            if chunk.choices:
                final_response += chunk.choices[0].message.content

        return final_response

    except Exception as e:
        print(f"Failed to call OpenAI API: {e}")
        return "Error: I'm having trouble accessing the knowledge sources right now."

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    query_results = query_engine(user_message)
    response = openai_chat(user_message, query_results)
    return jsonify({'text': response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
