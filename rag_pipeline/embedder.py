from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings_model():
    """
    Returns a HuggingFaceEmbeddings model.
    """
    # using a lightweight model for speed and local usage
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embeddings
