from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import create_plan
from execution.execution_manager import execute_plan

app = FastAPI(title="ORION")


class TaskRequest(BaseModel):
    goal: str


@app.post("/run-task")
def run_task(request: TaskRequest):

    plan = create_plan(request.goal)

    logs = execute_plan(plan)

    return {
        "goal": request.goal,
        "plan": plan,
        "status": "SUCCESS",
        "steps_executed": len(logs)
    }