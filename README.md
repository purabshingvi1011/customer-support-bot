# Customer Support Bot

A LangChain-powered customer support chatbot that answers questions from your internal documents.

## Features
- Ingests .txt / .pdf files from `data/support_docs`.
- Stores them as embeddings in a local ChromaDB vectorstore.
- Uses OpenRouter API (free tier for certain models).
- Quick CLI chat interface.

## Setup
1. **Install** dependencies: `pip install -r requirements.txt`
2. **Create .env** file from `.env.example`, add your `OPENROUTER_API_KEY`.
3. **Ingest** docs: `python ingest_docs.py`
4. **Run** bot: `python main.py`
5. **Ask** questions!
