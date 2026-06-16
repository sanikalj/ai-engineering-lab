"""from openai import OpenAI

client = OpenAI()
response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Quantum is the future of AI"
)

embedding= response.data[0].embedding
print(len(embedding))
print(embedding[:5])"""
import os
# This hides the HuggingFace Symlink warning completely
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
from sentence_transformers import SentenceTransformer

model= SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("I love coding in Python!")
print(embedding[:5])


