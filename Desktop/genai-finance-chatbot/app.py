# app.py

from dotenv import load_dotenv
import os

from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceInferenceAPI

# Load environment variables
load_dotenv()

# === Load documents ===
documents = SimpleDirectoryReader("data").load_data()

# === Define embedding model ===

embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# === Define a lightweight HuggingFace LLM === 
llm = HuggingFaceInferenceAPI(
    model_name="openai-community/gpt2",
    token=os.getenv("HF_API_TOKEN"),
    max_new_tokens=100,
    temperature=0.7,
)



# === Set global Settings
Settings.embed_model = embed_model
Settings.llm = llm

# === Build index and chat interface ===
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# === Chat Loop ===
while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        print("Goodbye you 💛")
        break
    response = query_engine.query(query)
    print(f"\n💬 Answer: {response}\n")
