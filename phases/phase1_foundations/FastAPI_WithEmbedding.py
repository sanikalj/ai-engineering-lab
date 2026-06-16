from fastapi import FastAPI
from sentence_transformers import SentenceTransformer

app = FastAPI()
print("Loading AI model... Please wait...")
model= SentenceTransformer("all-MiniLM-L6-v2")
print("AI model loaded successfully!")

@app.get("/get_embedding")
def calculateEmbedding(text:str):
    vector=model.encode(text)

    return {
        "original_text": text,
        "embedding_length": len(vector),
        "embedding": vector.tolist()
    }
