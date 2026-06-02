# =========================================================
# IMPORTS (ALL AT TOP - CLEAN STRUCTURE)
# =========================================================
import os
import pandas as pd
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from groq import Groq

# =========================================================
# ENV LOAD
# =========================================================
load_dotenv()

# =========================================================
# CONFIG
# =========================================================
CSV_PATH = "products_catalog_v2.csv"
PERSIST_DIRECTORY = "db/chroma_db"

# =========================================================
# GROQ SETUP
# =========================================================
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ API KEY NOT FOUND")

client = Groq(api_key=api_key)

print("✅ GROQ CLIENT READY")


# =========================================================
# DOCUMENT LOADING
# =========================================================
def load_documents():
    print("Loading CSV product catalog...\n")

    df = pd.read_csv(CSV_PATH)
    df.columns = df.columns.str.strip().str.lower()

    print("Total products:", len(df))

    docs = []

    for _, row in df.iterrows():
        text = "Product Information:\n"

        for col in df.columns:
            value = row.get(col, "")
            if pd.notna(value) and value != "":
                text += f"{col}: {value}\n"

        docs.append(Document(page_content=text, metadata=row.to_dict()))

    print("✅ Documents loaded successfully")
    return docs


# =========================================================
# CHUNKING
# =========================================================
def split_documents(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    print("Chunks created:", len(chunks))
    return chunks


# =========================================================
# VECTOR STORE 
# =========================================================
def create_vector_store(chunks):

    print("🔄 Creating embeddings...")

    embedding_model = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    print("✅ Vector DB ready")

    return db


# =========================================================
# PIPELINE 
# =========================================================

docs = load_documents()
chunks = split_documents(docs)
db = create_vector_store(chunks)

retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 8}
)


# =========================================================
# RAG FUNCTION 
# =========================================================
def ask_rag(question):

    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are an ecommerce AI assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

If product is not in context, say "Not available in catalog".
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception:
        return "⚠️ Limit reached. Try again later."
