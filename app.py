from fastapi import FastAPI
from env.environment import CustomerSupportEnv
from env.models import Action

app = FastAPI()
env = CustomerSupportEnv()

@app.get("/reset")
def reset():
    return env.reset("easy").dict()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()
