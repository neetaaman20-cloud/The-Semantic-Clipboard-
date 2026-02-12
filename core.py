import chromadb
from chromadb.utils import embedding_functions

# Initialize the local database
client = chromadb.PersistentClient(path="./clipboard_db")

# Use a lightweight, high-performance embedding model
embedding_model = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Get or create the collection for our clips
collection = client.get_or_create_collection(
    name="clips", 
    embedding_function=embedding_model
)

def add_clip(text, clip_id):
    """Adds a new text snippet to the vector database."""
    collection.add(
        documents=[text],
        ids=[clip_id]
    )

def search_clips(query, n_results=3):
    """Searches the database for the most relevant snippets."""
    return collection.query(
        query_texts=[query],
        n_results=n_results
    )