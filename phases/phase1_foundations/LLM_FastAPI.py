from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Sanjay,AI Engineering, Quantum"}

@app.get("/add")
async def add(a: int, b: int) -> dict:
    return {"result": a + b}

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
async def create_user(user: User):
    return {"message": f"User {user.name} created", "age": user.age}