import os
from openai import OpenAI
from env.environment import CustomerSupportEnv
from env.models import Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_task(task_name):
    env = CustomerSupportEnv()
    obs = env.reset(task_name)

    print(f"[START] task={task_name} env=customer-support model={MODEL_NAME}")

    step = 0
    rewards = []

    try:
        while True:
            step += 1

            prompt = f"User issue: {obs.user_message}\nWrite a helpful support response."

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}]
            )

            action_text = response.choices[0].message.content
            action = Action(response=action_text)

            obs, reward, done, info = env.step(action)

            rewards.append(f"{reward:.2f}")

            print(f"[STEP] step={step} action={action_text[:30]} reward={reward:.2f} done={str(done).lower()} error=null")

            if done or step >= 5:
                break

        print(f"[END] success={str(done).lower()} steps={step} rewards={','.join(rewards)}")

    except Exception:
        print(f"[END] success=false steps={step} rewards={','.join(rewards)}")

if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)
