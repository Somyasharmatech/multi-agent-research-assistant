from rag_pipeline.vector_store import VectorStore
from rag_pipeline.chunker import chunk_text

class RetrieverAgent:
    def __init__(self):
        self.vector_store = VectorStore()
        
    def index_content(self, text):
        """
        Chunks and indexes the provided text.
        """
        chunks = chunk_text(text)
        if chunks:
            self.vector_store.add_texts(chunks)
            
    def retrieve(self, query, k=3):
        """
        Retrieves relevant chunks for a query.
        """
        docs = self.vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]

if __name__ == "__main__":
    retriever = RetrieverAgent()
    # retriever.index_content("Some text about quantum computing.")
    # print(retriever.retrieve("quantum"))
