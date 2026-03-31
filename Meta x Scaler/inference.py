from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StepInput(BaseModel):
    state: dict = {}

@app.post("/reset")
def reset():
    return {
        "state": {"lanes": [10, 10, 10, 10]}
    }

@app.post("/step")
def step(input: StepInput):
    return {
        "state": {"lanes": [9, 11, 10, 10]},
        "reward": 1,
        "done": False
    }
