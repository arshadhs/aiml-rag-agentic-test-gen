
def retrieve_context(vectorstore, query: str, k: int = 4):
    """
    Retrieve relevant chunks from the vectorstore
    """

    # Call vectorstore.as_retriever()
    retriever = vectorstore.as_retriever(
        search_kwargs={"k":k}
    )

    docs = retriever.invoke(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    return context  # returns context text