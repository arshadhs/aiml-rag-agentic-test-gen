from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents(data_path: str = "data"):
    '''
    Load Project documents from the data folder
    '''

    loader = DirectoryLoader (
        data_path,
        glob="**/*.md",
        loader_cls=TextLoader
    )

    return loader.load()