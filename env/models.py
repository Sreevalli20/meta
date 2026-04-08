from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    ticket_id: int
    user_message: str
    status: str
    history: List[str]

class Action(BaseModel):
    response: str

class Reward(BaseModel):
    score: float
