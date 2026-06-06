# Pure Python concept of RAG generation
def basic_rag_prompt(user_query, retrieved_chunks):
    context = "\n".join(retrieved_chunks)
    prompt = f"""Use the Context below to answer the Query. If unsure, say "I don't know".

    Context:
    {context}

    Query: {user_query}
    Answer:"""
    return prompt


chunks = ["ACME corp profits grew by 42% in 2025.", "ACME corp CEO is Jane Doe."]
print(basic_rag_prompt("How did ACME perform in 2025?", chunks))
