from flask import Flask, request, jsonify
import os
import shutil
import openai
import chromadb
import getpass
from openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from IPython.display import Markdown, display
from llama_index.embeddings.openai import OpenAIEmbedding

client = OpenAI()

# OpenAI API setup
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass.getpass("OpenAI API Key:")
openai.api_key = os.environ["OPENAI_API_KEY"]

# ChromaDB setup 
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

embed_model = OpenAIEmbedding(
    model="text-embedding-3-large",
    dimensions=1536,
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

# Helper functions
def check_database_exists():
    return os.path.exists("./chroma_db")

def rebuild_database():
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )

def query_engine(user_message):
    engine = index.as_query_engine(similarity_top_k=5)
    query_results = engine.query(user_message)
    return query_results

# OpenAI interaction function
def openai_chat(user_message, query_results):
    try:
        augmented_prompt = f"""
            **Instructions:** Carefully answer the user's question using the provided database information. Here's some context to help you:

            * **Database Content:** This database contains information for Philips Healthcare Patient Monitoring.  
            * **Focus:** Extract the most relevant details from the database results to address the user's query directly, if you dont know say so.
            * **Answer Style:** Provide an answer that is concise, detailed, includes comparisons, and use bullet points. OUTPUT IN MARKDOWN.

            **Database Results:**
            {query_results}

            **User Query:**
            {user_message}

            **Answer:** 
            """ 

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": augmented_prompt}],
            temperature=0.95,  # Change to float
            max_tokens=4095,   # Change to integer
            top_p=1.0,         # Change to float
            stream=True
        )

        final_response = ""
        for chunk in response:
            if chunk.choices and len(chunk.choices) > 0:
                content = chunk.choices[0].delta.content if chunk.choices[0].delta.content is not None else ''
                final_response += content

        return final_response.strip()  # Remove leading/trailing whitespace

    except Exception as e:
        print(f"Failed to call OpenAI API: {e}")
        return "Error: I'm having trouble accessing the knowledge sources right now."

# Flask app setup
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    query_results = query_engine(user_message)
    response = openai_chat(user_message, query_results)
    return jsonify({'text': response})

# Main interaction loop
if __name__ == "__main__":
    app.run(debug=True)
