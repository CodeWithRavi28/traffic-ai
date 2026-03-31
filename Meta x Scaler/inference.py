from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class ActionInput(BaseModel):
    state: dict = {}

@app.post("/reset")
def reset():
    return {
        "state": {"lanes": [10, 10, 10, 10]}
    }

@app.post("/step")
def step(input: ActionInput):
    lanes = input.state.get("lanes", [10, 10, 10, 10])
    action = random.randint(0, 3)
    lanes[action] = max(0, lanes[action] - 1)

    return {
        "state": {"lanes": lanes},
        "reward": 1,
        "done": False
    }
