import chromadb
from openai import OpenAI

client = OpenAI()
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="quantum_docs")

query = "Explain superposition"
query_embedding = client.embeddings.create(
    model="qwen2.5-coder:1.5b",
    input=query
).data[0].embedding

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)
context = "\n".join(results["documents"][0])

answer = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a quantum expert."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]
)

print(answer.choices[0].message.content)
#tinyllama

