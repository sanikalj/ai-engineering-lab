from openai import api_key
from openai.types import embedding
from pinecone import Pinecone

pc= Pinecone(api_key="your key")
index=pc.Index("quantum-index")

index.upsert([
    ("doc1", embedding),
])
query_result = index.query(
    vector=embedding,
    top_k=3,
    include_metadata=True
)

print(query_result)

