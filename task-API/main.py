from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()


class NewTask(BaseModel):
    title: str


tasks = {
    1: {"id": 1, "title": "Learn FastAPI", "completed": False},
    2: {"id": 2, "title": "Build an API", "completed": False},
}

API_KEY = "secret123"


@app.get("/task")
def get_tasks():
    return list(tasks.values())


@app.get("/task/{task_id}")
def get_task_by_id(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.post("/task", status_code=201)
def create_task(task: NewTask, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    new_id = max(tasks.keys()) + 1 if tasks else 1
    new_task = {"id": new_id, "title": task.title, "completed": False}
    tasks[new_id] = new_task
    return new_task