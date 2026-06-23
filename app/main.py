"""
AIML RAG Agentic Test Generator

Main entry point for the project.

This script initialises the application, loads environment variables,
connects to the LLM provider, and runs the first test-generation workflow.

Project:
    aiml-rag-agentic-test-gen

Author:
    Arshad Siddiqui

Description:
    This project uses Retrieval-Augmented Generation (RAG), Large Language
    Models (LLMs), and agentic AI workflows to generate software test cases
    from requirements, source code, documentation, and existing tests.
"""
print("main.py started")
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI             # LLM Provider

from dotenv import load_dotenv                      # Load environment variables

from rag.loader import load_documents               # Import document loader function
from rag.splitter import split_documents            # Import text chunking function
from rag.vector_store import create_vector_store    # Import database creator function
from rag.retriever import retrieve_context          # Import similarity search function

def main():
    print("load_dotenv...")
    load_dotenv()    # Read API keys from .env file

    # RAG - Pipeline Ingestion & Encoding
    # documents = load_documents("data")          # 1. Load Directory
    # chunks = split_documents(documents)         # 2. Split Data
    # vectorstore = create_vector_store(chunks)   # 3. Create vector store (Embed text chunks and save to DB)

    print("Step 1: about to load documents")
    documents = load_documents("data")
    print(f"Step 1 done: loaded {len(documents)} documents")

    print("Step 2: about to split documents")
    chunks = split_documents(documents)
    print(f"Step 2 done: created {len(chunks)} chunks")

    print("Step 3: about to create vector store")

    try:
        vectorstore = create_vector_store(chunks)
        print("Step 3 done: vector store created")
    except BaseException as e:
        print("Error while creating vector store")
        print(type(e).__name__)
        print (e)
        return

    print(f"Loaded documents: {len(documents)}")
    print(f"Created chunks: {len(chunks)}")

    # RAG - Retrieval
    task = "Generate pytest unit tests for login with invalid passwords and locked accounts."

    # Pass vectorstore to retriever
    context = retrieve_context(
        vectorstore = vectorstore,  # Target database to query
        query = task,               # Search string based on the task
        k = 4                       # Fetch top 4 most relevant chunks
    )
    print(f"Retrieved context length: {len(context)} characters")

    # Instruction Setup
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert software test engineer."),
        ("human", """
        Use the following project context to generate pytest tests.

Context:
{context}

Task:
{task}

Rules:
- Return only valid pytest code.
- Do not include explanations outside the code.
- Use clear test function names.
- Use simple in-memory dictionaries for test data.
- Assert both the `success` and `message` fields.
""")
    ])

    # Initialize a chat model from any supported provider using a unified interface.

    # claude-sonnet-4-5
    # temperature: Model temperature for controlling randomness.
    # model = init_chat_model("openai:gpt-5.5", temperature=0) 
    # model.invoke("what's your name")

    llm = ChatOpenAI(
            model ="gpt-4o-mini",
            temperature=0.2
        )

    #response = llm.invoke("Explain unit testinf in simple terms.")
   
    # Chain Assembly
    chain = prompt | llm

    # Pipeline Generation Execution
    print("Generating pytest tests...")
    response = chain.invoke({
        "context": context,
        "task": task
        })

    # Output
    print("---------------------")
    print(response.content)

if __name__ == "__main__":
    main()