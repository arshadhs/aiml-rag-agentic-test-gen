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

from langchain.tools import tool
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize a chat model from any supported provider using a unified interface.

# claude-sonnet-4-5
# temperature: Model temperature for controlling randomness.
# model = init_chat_model("openai:gpt-5.5", temperature=0) 
# model.invoke("what's your name")

llm = ChatOpenAI(
    model ="gpt-4o-mini",
    temperature=0.2
    )
    
response = llm.invoke("Explain unit testinf in simple terms.")

print(response.content)