import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate

def run_bot():
    load_dotenv()

    print("🤖 Customer Support Bot (type 'exit' or 'quit' to leave)\n")

    # Set up embedding model (same as used in ingest_docs.py)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )
    retriever = vectorstore.as_retriever()

    # Set up chat model using OpenRouter
    llm = ChatOpenAI(
        temperature=0.0,
        model_name="openai/gpt-3.5-turbo",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=os.getenv("OPENROUTER_API_KEY")
    )

    # Custom prompt for better accuracy
    custom_prompt = PromptTemplate(
        template="""You are a helpful customer support assistant. Use the following document excerpts to answer the question as accurately as possible.

If the answer is not in the documents, say "I'm not sure, please contact customer support."

Question: {question}
=========
{context}
=========
Answer:""",
        input_variables=["context", "question"]
    )

    # QA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": custom_prompt},
        return_source_documents=True
    )

    # Chat loop
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        response = qa_chain(query)
        answer = response["result"]
        sources = response["source_documents"]

        print(f"\n🤖 Bot: {answer}")
        if sources:
            print("Sources used:")
            for doc in sources:
                print(f" - {doc.metadata.get('source', 'Unknown')}")
        print()

if __name__ == "__main__":
    run_bot()
