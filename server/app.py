from fastapi import FastAPI
from env.environment import CustomerSupportEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = CustomerSupportEnv()

@app.get("/")
def home():
    return {"message": "OpenEnv is running"}

@app.api_route("/reset", methods=["GET", "POST"])
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

# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
