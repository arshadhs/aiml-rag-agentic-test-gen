'''
pip install langchain
pip install langgraph
pip install langchain-opena


pip install langchain langchain-openai langchain-community chromadb python-dotenv tiktoken pytest coverage
'''

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

print(response.context)