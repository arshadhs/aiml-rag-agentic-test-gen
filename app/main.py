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

print("aiml-rag-agentic-test-gen: Started")

import sys

# For debugging
# import atexit
# atexit.register(lambda: print(f"[atexit] process exiting, last exception: {sys.exc_info()}"))

from pathlib import Path
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
        print(f"Step 3 done: vector store type={type(vectorstore)}, value={vectorstore}")
    except BaseException as e:
        import traceback
        print("Error while creating vector store")
        print(f"{type(e).__name__}: {e}")
        traceback.print_exc()
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
- Do not include Markdown code fences.
- Do not include explanations outside the code.
- Do not redefine or reimplement the application code.
- Import the function under test from the application source code.
- Use: from app.auth_service import login
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

    # Save generated tests to file
    outout_dir = PROJECT_ROOT / "generated_tests" / "python"
    outout_dir.mkdir(parents=True, exist_ok=True)

    output_file = outout_dir / "test_auth_service_generated.py"

    clean_code = response.content.strip()

    # Remove markdown (if model includes them)
    if clean_code.startswith("```python"):
        clean_code = clean_code.replace("```python", "", 1).strip()

    if clean_code.startswith("```"):
        clean_code = clean_code.replace("```", "", 1).strip()

    if clean_code.endswith("```"):
        clean_code = clean_code.replace("```", "", 1).strip()
        
    output_file.write_text(clean_code, encoding="utf-8")

    print(f"\naiml-rag-agentic-test-gen: Generated tests saved to: {output_file}")

if __name__ == "__main__":
    main()