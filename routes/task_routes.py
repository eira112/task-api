from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.db_models import Task
from models.task_models import TaskCreate


router = APIRouter()
@router.post("/tasks", status_code=201)
def create_task(task: TaskCreate, db:Session=Depends(get_db)):
    new_task= Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "task created", "task": new_task}

@router.get("/tasks")
def get_tasks(db: Session=Depends(get_db)):
    tasks=db.query(Task).all()
    return tasks

@router.get("/tasks/{task_id}")
def get_task(task_id: int, db:Session=Depends(get_db)):

    task = db.get(Task,task_id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    return task

@router.put("/tasks/{task_id}")
def complete_task(task_id: int, db: Session=Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    task.completed=True
    db.commit()
    db.refresh(task)

    return task

@router.delete("/tasks/{task_id}")
def remove_task(task_id: int, db:Session=Depends(get_db)):
    task = db.get(Task, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    db.delete(task)
    db.commit()

    return {"message": "task removed from the list"}