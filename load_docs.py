from langchain_community.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_json(path):
    """
    Loads a JSON file where each item has a 'chunk' and 'metadata' field.

    Assumes the JSON file is an array of objects like:
    [
        {
            "chunk": "Text content...",
            "metadata": {
                "source": "Source name",
                "section": "Section name",
                "keywords": [...]
            }
        },
        ...
    ]

    Parameters:
        path (str): Path to the JSON file.

    Returns:
        List[Document]: A list of LangChain Document objects with metadata.
    """
    loader = JSONLoader(
        file_path=path,
        jq_schema=".[] | {text: .chunk, metadata: .metadata}",
        text_content=False
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)
