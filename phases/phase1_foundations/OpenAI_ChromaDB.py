import chromadb
client= chromadb.Client()
collection = client.create_collection(name="quantum_docs")
collection.add(
    documents=[
        "Quantum computing uses qubits.",
        "Entanglement is a key quantum phenomenon.",
        "Superposition allows qubits to be in multiple states."
    ],
    ids=["doc1", "doc2", "doc3"]
)
results = collection.query(
    query_texts=["What is entanglement?"],
    n_results=1
)
print(results)