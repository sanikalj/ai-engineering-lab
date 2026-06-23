#Step 1: Our private "Knowledge Base" (The Reference Book)
knowledge_base={
    "project_alpha": "Project Alpha is a secret rocket project launching in 2028.",
    "project_beta": "Project Beta is our new eco-friendly office garden initiative."
}
# The user's question
user_question="When is the secret rocket project launching?"
# --- THE RAG PROCESS ---
# 1. RETRIEVAL: Find the relevant document matching the question
retrieved_info=""
for key, text in knowledge_base.items():
    if "rocket" in text:
        retrieved_info=text
# 2. AUGMENTATION: Combine the found info with the question to create a prompt
prompt = f"Answer the question based only on this context:\nContext: {retrieved_info}\nQuestion: {user_question}"
# 3. GENERATION: Simulating sending this prompt to an AI model
print("--- Prompt Sent to AI ---")
print(prompt)