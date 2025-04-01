import os
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

def ingest_docs():
    load_dotenv()  # Load OPENROUTER_API_KEY from .env

    folder_path = "data/support_docs"
    docs = []

    # Collect all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") or filename.endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            print(f"Loading: {full_path}")
            loader = UnstructuredFileLoader(full_path)
            docs.extend(loader.load())

    # Split large documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)

    print(f"🔎 Loaded {len(docs)} documents. Split into {len(chunks)} chunks.")

    # Build embeddings + local vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )


    vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="vectorstore")
    vectorstore.persist()

    print("✅ Ingestion complete! Vectorstore saved to 'vectorstore/'.")

if __name__ == "__main__":
    ingest_docs()
