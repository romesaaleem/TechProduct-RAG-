
**TechProduct_RAG_System**

An AI-powered ecommerce chatbot built using **Retrieval-Augmented Generation (RAG)** architecture for intelligent product search and context-aware responses.

**Table of Contents**

* [Overview](#overview)
* [Problem Statement](#problem-statement)
* [Project Architecture](#project-architecture)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Files](#project-files)
* [How It Works](#how-it-works)
* [Installation](#installation)
* [How to Run the Project](#how-to-run-the-project)
* [Sample Queries](#sample-queries)
* [Deployment](#deployment)
* [Results](#results)
* [Future Improvements](#future-improvements)
* [Project Configuration Files](#project-configuration-files)
* [Author](#author)

**Overview**

**TechProduct_RAG_System** is an AI-powered ecommerce assistant that enables users to search and retrieve product information using natural language queries.

Instead of keyword-based search, it uses **RAG (Retrieval-Augmented Generation)** with embeddings to understand intent and deliver context-aware responses.


**Problem Statement**

Traditional ecommerce search systems:

* Fail to understand intent
* Depend only on keywords
* Provide irrelevant results for complex queries

This project solves it using **semantic AI search**.


**Project Architecture**

**Workflow:**

1. Load product catalog (CSV)
2. Convert into LangChain documents
3. Split into chunks
4. Generate embeddings (Hugging Face)
5. Store in ChromaDB
6. Retrieve relevant chunks via similarity search
7. Pass context to Groq LLM
8. Generate response
9. Show in Gradio UI

**Features**

* AI-powered ecommerce chatbot
* Semantic search (not keyword-based)
* RAG pipeline implementation
* Context-aware responses
* ChromaDB vector database
* Hugging Face embeddings
* Groq LLM integration
* Gradio chatbot UI
* Real-time responses

**Technologies Used**

**Language:** Python

**Libraries:**

* LangChain
* ChromaDB
* Hugging Face Transformers
* Groq API
* Gradio
* Pandas
* python-dotenv

**Models:**

* llama-3.3-70b-versatile
* all-MiniLM-L6-v2

**Project Files**

### `rag_backend.py`

Handles:

* Data loading
* Chunking
* Embeddings
* Vector DB
* Retrieval
* LLM responses

### `app.py`

Handles:

* Gradio UI
* Chat interface
* Frontend logic

---

# ⚙ How It Works

## 1. Load Dataset

```text
products_catalog_v2.csv
```

## 2. Chunking

* Chunk size: 500
* Overlap: 100

## 3. Embeddings

* Model: all-MiniLM-L6-v2

## 4. Vector DB

* ChromaDB stores embeddings

## 5. Retrieval

* Similarity search (k=8)

## 6. Response Generation

* LLM: llama-3.3-70b-versatile via Groq

# 🚀 Installation

```bash
git clone https://github.com/romesaaleem/TechProduct_RAG_System.git
cd TechProduct_RAG_System
pip install -r requirements.txt
```

---

# ▶ How to Run the Project

## 1. Create `.env`

```env
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

## 2. Add Dataset

```text
products_catalog_v2.csv
```

## 3. Run App

```bash
python app.py
```

## 4. Open Browser

```text
http://127.0.0.1:7860
```

---

# 💬 Sample Queries

* Best gaming laptop under budget
* Show HP Victus specs
* RTX laptops under 1500$
* Best battery phone
* Lenovo Legion price

---

# 🌐 Deployment

* Hugging Face Spaces
* Gradio UI

### Secrets Required:

* GROQ_API_KEY
* HF_TOKEN

---

# 📊 Results

* Improved semantic search accuracy
* Better intent understanding
* Faster product discovery
* Context-aware responses

---

# 🔮 Future Improvements

* Memory-based chatbot
* Hybrid search (BM25 + embeddings)
* Recommendation engine
* Multi-language support
* User authentication
* Cloud vector DB

---

# 📁 Project Configuration Files

## requirements.txt

```txt
pandas
langchain
langchain-community
langchain-core
langchain-text-splitters
langchain-chroma
chromadb
sentence-transformers
gradio
groq
python-dotenv
```

## .env

```env
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

## .gitignore

```gitignore
.env
__pycache__/
*.pyc
venv/
```


**Author
**
**Romesa Aleem**
📧 [romesaaleem29@gmail.com](mailto:romesaaleem29@gmail.com)
🔗 LinkedIn Profile

