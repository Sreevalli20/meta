from env.models import Observation, Action
from env.tasks import TASKS
from env.grader import grade

class CustomerSupportEnv:
    def __init__(self):
        self.current_task = None
        self.done = False
        self.history = []

    def reset(self, task_name="easy"):
        self.current_task = TASKS[task_name]
        self.done = False
        self.history = []

        return Observation(
            ticket_id=self.current_task["ticket_id"],
            user_message=self.current_task["message"],
            status="open",
            history=[]
        )

    def step(self, action: Action):
        if self.done:
            return None, 0.0, True, {}

        self.history.append(action.response)
        score = grade(action.response, self.current_task["expected"])

        reward = score * 0.8
        done = score > 0.7

        if done:
            reward += 0.2

        self.done = done

        obs = Observation(
            ticket_id=self.current_task["ticket_id"],
            user_message=self.current_task["message"],
            status="resolved" if done else "open",
            history=self.history
        )

        return obs, reward, done, {"score": score}

    def state(self):
        return {
            "task": self.current_task,
            "history": self.history,
            "done": self.done
        }
