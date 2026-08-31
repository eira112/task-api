from fastapi import APIRouter, HTTPException

from models.task_models import TaskCreate
from task_manager import (
    add_task,
    find_task,
    complete_task as mark_complete,
    delete_task,
)

router = APIRouter()

tasks = []


@router.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    add_task(tasks, task.title)
    return {"message": "task created", "task": tasks[-1]}


@router.get("/tasks")
def get_tasks():
    return tasks


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(tasks, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    return task


@router.put("/tasks/{task_id}")
def complete_task(task_id: int):
    task = find_task(tasks, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    mark_complete(task)

    return task


@router.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    task = find_task(tasks, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    delete_task(tasks, task)

    return {"message": "task removed from the list"}