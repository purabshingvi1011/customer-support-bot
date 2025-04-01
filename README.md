# Customer Support Bot 🤖

A LangChain-powered AI chatbot for answering customer queries using your own documents (FAQs, policies, etc.).  
Built with:

- 🔍 **Chroma** for document search (vectorstore)
- 🧠 **HuggingFace Embeddings** for free, local text embeddings
- 💬 **OpenRouter (GPT-3.5)** for generating chat responses
- ⚡ CLI and ready for Streamlit upgrade

---

## 🚀 Features

- Ask questions like “What is our return policy?” or “Do we offer international shipping?”
- Supports `.txt` and `.pdf` files in the `data/support_docs/` folder
- Uses Retrieval-Augmented Generation (RAG) with LangChain
- Fully open-source and budget-friendly (no OpenAI costs)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-support-bot.git
cd customer-support-bot
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> If you face issues with sentence-transformers, try:
```bash
pip install sentence-transformers==2.2.2 huggingface-hub==0.17.3 transformers==4.33.1
```

---

## 🔐 Environment Variables

Create a `.env` file with:

```bash
OPENROUTER_API_KEY=YOUR_API_KEY
```

Get a free API key from https://openrouter.ai

---

## 📄 Add Support Docs

Put your support documents in:

```
data/support_docs/
```

Example:
```txt
Q: What is our return policy?
A: You can return any product within 30 days of purchase.

Q: Do we offer international shipping?
A: Yes, we ship globally.
```

---

## ⚙️ Run the Bot

### 1. Ingest Documents
```bash
python ingest_docs.py
```

### 2. Start Chatbot (CLI)
```bash
python main.py
```

Then ask your questions!

---

## 📦 Project Structure

```
customer_support_bot/
│
├── main.py              # Chat interface
├── ingest_docs.py       # Doc ingestion
├── requirements.txt     # Python dependencies
├── .env.example         # API key template
├── data/support_docs/   # Your FAQ or policy docs
└── vectorstore/         # Auto-created DB (Chroma)
```

---

## ✨ Credit

Built using:
- LangChain
- OpenRouter
- Hugging Face
- ChromaDB
