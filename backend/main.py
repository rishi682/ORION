from fastapi import FastAPI
from pydantic import BaseModel

from backend.agents.planner import create_plan
from backend.execution.execution_manager import execute_plan

app = FastAPI(title="ORION")


class TaskRequest(BaseModel):
    goal: str


@app.post("/run-task")
def run_task(request: TaskRequest):

    plan = create_plan(request.goal)

    results = execute_plan(request.goal)

    return {
        "goal": request.goal,
        "plan": plan,
        "results": results,
        "status": "SUCCESS"
    }