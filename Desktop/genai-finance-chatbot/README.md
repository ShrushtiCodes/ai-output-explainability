# 🧠 GenAI Finance Chatbot (RAG-powered)

A lightweight Retrieval-Augmented Generation (RAG) chatbot built using LlamaIndex and HuggingFace, designed to answer questions based on your **own custom financial documents**.

> 💡 Works completely free using HuggingFace-hosted LLMs — no OpenAI needed.

---

## 📌 Key Features

- 🧾 Ingest documents from a local `/data` folder
- 📚 Build vector index with `sentence-transformers`
- 💬 Query using HuggingFace LLMs (GPT2, Flan, Falcon, etc.)
- 🛠️ Modular: swap in your own LLMs or vector DB
- 🧃 Free-tier friendly (great for demo & prototyping)

---

## 🧠 How It Works

1. Loads documents using `SimpleDirectoryReader`
2. Generates embeddings using HuggingFace (MiniLM)
3. Creates a vector store index using LlamaIndex
4. Uses an LLM to answer questions based on retrieved context

---

## 🛠 Tech Stack

- `llama-index`
- `sentence-transformers`
- `chromadb`
- `huggingface_hub`
- `python-dotenv`

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/genai-finance-chatbot.git
cd genai-finance-chatbot

Built with ❤️ by [Shrushti](https://github.com/ShrushtiCodes)
