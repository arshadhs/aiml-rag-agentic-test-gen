from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size: int = 1000, chunk_overlap:int = 150):
    """
    Split loaded doc into smaller chunks for retireval.
    """
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    return splitter.split_documents(documents)