from fastapi.testclient import TestClient
from main import app
from database import SessionLocal
from models.db_models import Task
import pytest

client=TestClient(app)

@pytest.fixture
def clean_tasks():
    db=SessionLocal()
    def cleanup(task_id):
        task=db.get(Task,task_id)
        if task:
            db.delete(task)
            db.commit()
    yield cleanup
    db.close()


def test_home():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={"message":"task api is running"}

def test_create_task(clean_tasks):
    response=client.post("/tasks", json={"title":"add authentication"})
    task_id=response.json()["task"]["id"]
    assert response.status_code==201
    assert response.json()=={"message":"task created","task":{"id":task_id,"title":"add authentication","completed":False}}
    clean_tasks(task_id)

def test_get_tasks(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response=client.get("/tasks")
    tasks=response.json()
    current_task=None
    for task in tasks:
        if(task["id"]==task_id):
            current_task=task
    assert response.status_code==200
    assert current_task=={"id":task_id,"title":"test task","completed":False}
    clean_tasks(task_id)

def test_get_task(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response=client.get(f"/tasks/{task_id}")
    assert response.status_code==200
    assert response.json()=={"id":task_id,"title":"test task","completed":False}
    clean_tasks(task_id)

def test_complete_task(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response= client.put(f"/tasks/{task_id}")
    assert response.status_code==200
    assert response.json()=={"id":task_id,"title":"test task","completed":True}
    clean_tasks(task_id)

def test_delete_task(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response= client.delete(f"/tasks/{task_id}")
    assert response.status_code==200
    assert response.json()=={"message":"task removed from the list"}

