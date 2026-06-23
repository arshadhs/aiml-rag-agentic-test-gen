'''
 Creates Chroma Vector Store
'''
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def create_vector_store(chunks, persist_directory: str = "chroma_db"):
    '''
    Create a Chroma Vector Store from document chunks.
    '''

    print("vector_store.py: creating OpenAI embeddings object...")
    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small"
    )

    print("vector_store.py: embeddings object created")
    print(f"vector_store.py: number of chunks received: {len(chunks)}")
    print("vector_store.py: creating Chroma vector store...")
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    print("vector_store.py: Chroma vector store created")

    return vectorstore