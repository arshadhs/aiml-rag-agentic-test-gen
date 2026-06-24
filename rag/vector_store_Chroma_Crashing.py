'''
 Creates Chroma Vector Store
'''
import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def _not_using_create_vector_store(chunks, persist_directory: str = "chroma_db"):
    '''
    Create a Chroma Vector Store from document chunks.
    '''

    print("vector_store.py: [OpenAIEmbeddings] creating OpenAI embeddings object...")
    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small"
    )
    print("vector_store.py: embeddings object created")
    print(f"vector_store.py: number of chunks received: {len(chunks)}")


    # Test embeddings object work before touching Chroma
    print("vector_store.py: [embed_query] testing embeddings...")
    test = embeddings.embed_query("test")
    print(f"vector_store.py: embedding test OK, dimension={len(test)}")

    # Explicit persistent client — required for chromadb 1.x
    print("vector_store.py: [PersistentClient] creating Chroma vector store...")
    client = chromadb.PersistentClient(path=persist_directory)

    try:
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            client=client,
            collection_name="documents",  # explicit name avoids default collision
        )
    except Exception as e:
        print(f"vector_store.py: [Chroma.from_documents] Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exex()
        raise

    print("vector_store.py: Chroma vector store created")

    return vectorstore