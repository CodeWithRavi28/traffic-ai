from fastapi import FastAPI

app = FastAPI()

@app.post("/reset")
def reset():
    return {"message": "Environment reset"}

@app.post("/step")
def step():
    return {"action": 0}
