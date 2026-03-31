from fastapi import FastAPI
import random

app = FastAPI()

state = {"lanes": [10, 10, 10, 10]}

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/reset")
def reset():
    global state
    state = {"lanes": [10, 10, 10, 10]}
    return {"state": state}

@app.post("/step")
def step():
    global state
    action = random.randint(0, 3)
    state["lanes"][action] = max(0, state["lanes"][action] - 1)

    return {
        "state": state,
        "reward": 1,
        "done": False
    }
