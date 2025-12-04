from langchain_community.vectorstores import FAISS
from rag_pipeline.embedder import get_embeddings_model
from config.settings import settings
import os

class VectorStore:
    def __init__(self):
        self.embeddings = get_embeddings_model()
        self.index_path = settings.VECTOR_DB_PATH
        self.db = None
        
    def create_index(self, texts, metadatas=None):
        """
        Creates a new FAISS index from texts.
        """
        self.db = FAISS.from_texts(texts, self.embeddings, metadatas=metadatas)
        return self.db

    def add_texts(self, texts, metadatas=None):
        """
        Adds texts to the existing index or creates a new one.
        """
        if self.db is None:
            self.create_index(texts, metadatas)
        else:
            self.db.add_texts(texts, metadatas=metadatas)
            
    def similarity_search(self, query, k=5):
        """
        Performs similarity search.
        """
        if self.db is None:
            return []
        return self.db.similarity_search(query, k=k)
    
    def save_index(self):
        """
        Saves the index to disk.
        """
        if self.db:
            self.db.save_local(self.index_path)
            
    def load_index(self):
        """
        Loads the index from disk.
        """
        if os.path.exists(self.index_path):
            self.db = FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)
        else:
            print("Index not found.")
