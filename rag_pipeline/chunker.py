from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import settings

def chunk_text(text, chunk_size=None, chunk_overlap=None):
    """
    Splits text into chunks using RecursiveCharacterTextSplitter.
    """
    if chunk_size is None:
        chunk_size = settings.CHUNK_SIZE
    if chunk_overlap is None:
        chunk_overlap = settings.CHUNK_OVERLAP
        
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return text_splitter.split_text(text)
