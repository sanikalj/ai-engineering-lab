import chromadb
import ollama  # pip install ollama

# 1. Setup Local ChromaDB (Free/Local)
db_client = chromadb.Client()
collection = db_client.get_or_create_collection("free_quantum_docs")

# 2. Add data (ChromaDB handles embeddings locally for free)
collection.add(
    documents=[
        "Quantum computing uses qubits.",
        "Entanglement is a key quantum phenomenon.",
        "Superposition allows qubits to be in multiple states."
    ],
    ids=["doc1", "doc2", "doc3"]
)

# 3. Search (The query is also embedded locally for free)
query = "Explain superposition"
results = collection.query(
    query_texts=[query], # Use query_texts instead of manual embeddings
    n_results=1
)
context = results["documents"][0][0]

# 4. Generate Answer using local LLM (Ollama)
response = ollama.chat(
    model='tinyllama',
    messages=[
        {'role': 'system', 'content': 'You are a quantum expert.'},
        {'role': 'user', 'content': f"Context: {context}\n\nQuestion: {query}"}
    ]
)

print(response['message']['content'])

