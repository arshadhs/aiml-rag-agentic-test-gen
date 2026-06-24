"""
Creates a simple in-memory vector store.

Avoid ChromaDB for MVP and keeps the RAG pipeline working.
"""

import math
from langchain_openai import OpenAIEmbeddings

def cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two vectors.
    """
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)


class SimpleRetriever:
    """
    Simple retriever that returns the top-k most similar documents.
    """

    def __init__(self, documents, vectors, embeddings, k=4):
        self.documents = documents
        self.vectors = vectors
        self.embeddings = embeddings
        self.k = k

    def invoke(self, query):
        query_vector = self.embeddings.embed_query(query)

        scored_documents = []

        for document, vector in zip(self.documents, self.vectors):
            score = cosine_similarity(query_vector, vector)
            scored_documents.append((score, document))

        scored_documents.sort(key=lambda item: item[0], reverse=True)

        return [document for score, document in scored_documents[:self.k]]


class SimpleVectorStore:
    """
    Simple vector store with an as_retriever() method.
    This keeps compatibility with your existing retriever.py file.
    """

    def __init__(self, documents, vectors, embeddings):
        self.documents = documents
        self.vectors = vectors
        self.embeddings = embeddings

    def as_retriever(self, search_kwargs=None):
        search_kwargs = search_kwargs or {}
        k = search_kwargs.get("k", 4)

        return SimpleRetriever(
            documents=self.documents,
            vectors=self.vectors,
            embeddings=self.embeddings,
            k=k
        )


def create_vector_store(chunks, persist_directory: str = "chroma_db"):
    """
    Create an in-memory vector store from document chunks.
    """

    print("vector_store.py: creating OpenAI embeddings object...")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    print("vector_store.py: embeddings object created")
    print(f"vector_store.py: number of chunks received: {len(chunks)}")
    print("vector_store.py: creating embeddings for chunks...")

    texts = [chunk.page_content for chunk in chunks]
    vectors = embeddings.embed_documents(texts)

    print("vector_store.py: embeddings created")
    print("vector_store.py: creating simple vector store...")

    vectorstore = SimpleVectorStore(
        documents=chunks,
        vectors=vectors,
        embeddings=embeddings
    )

    print("vector_store.py: simple vector store created")

    return vectorstore