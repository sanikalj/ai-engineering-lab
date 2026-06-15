from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def greet_user():
    return {"message": "Hello! Welcome to our store."}

@app.get("/")
def base_url():
    return {"You have just hit the base URL 127.0.0.0:8000"}