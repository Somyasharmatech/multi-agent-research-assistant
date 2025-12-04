import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    # Add other keys as needed, e.g., SERPER_API_KEY if using Serper
    
    # Model Configuration
    MODEL_NAME = "llama-3.3-70b-versatile" # Updated to supported model
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    VECTOR_DB_PATH = os.path.join(BASE_DIR, "faiss_index")
    
    # RAG Configuration
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    
settings = Settings()
