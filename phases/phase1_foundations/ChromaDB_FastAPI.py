from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import chromadb
from typing import List, Optional

# 1. Initialize FastAPI app
app = FastAPI(
    title="Quantum Library Semantic Search API",
    description="Search library documents using ChromaDB and FastAPI",
    version="1.0.0"
)

# 2. Initialize ChromaDB Client (Ephemeral/In-Memory)
chroma_client = chromadb.EphemeralClient()
collection = chroma_client.get_or_create_collection(name="library_collection")

# Seed the database with your sample document if empty
if collection.count() == 0:
    collection.add(
        documents=["entanglement is a key quantum phenomenon."],
        ids=["doc2"],
        metadatas=[{"category": "physics"}]
    )


# 3. Define Pydantic models for structured API responses
class SearchResultItem(BaseModel):
    id: str
    document: str
    distance: float
    metadata: Optional[dict] = None


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResultItem]

@app.get("/")
async def root():
    return {"message": "Welcome to the Quantum Library API! Go to /search?q=your_query to search."}

# 4. Create the GET search endpoint
@app.get("/search", response_model=SearchResponse)
async def search_library(
        q: str = Query(..., description="The search query text"),
        n_results: int = Query(5, description="Number of results to return")
):
    try:
        # Query ChromaDB using the text parameter
        query_results = collection.query(
            query_texts=[q],
            n_results=n_results
        )

        formatted_results = []

        # Safely extract the inner lists from Chroma's batched responses
        # Chroma returns lists of lists: e.g., documents=[['doc_text_1', 'doc_text_2']]
        if query_results["documents"] and len(query_results["documents"]) > 0:
            ids = query_results["ids"][0]
            documents = query_results["documents"][0]
            distances = query_results["distances"][0]
            metadatas = query_results["metadatas"][0] if query_results["metadatas"] else [None] * len(ids)

            # Safely iterate through elements inside the batch list
            for i in range(len(documents)):
                item = SearchResultItem(
                    id=ids[i],
                    document=documents[i],
                    distance=distances[i],
                    metadata=metadatas[i]
                )
                formatted_results.append(item)

        return SearchResponse(query=q, results=formatted_results)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("LLM_FastAPI:app", host="127.0.0.1", port=8000, reload=True)
