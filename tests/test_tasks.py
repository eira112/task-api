from fastapi.testclient import TestClient
from main import app
from routes.task_routes import tasks
import pytest

client=TestClient(app)

@pytest.fixture
def clean_tasks():
    tasks.clear()

def test_home():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={"message":"task api is running"}

def test_create_task(clean_tasks):
    response=client.post("/tasks", json={"title":"add authentication"})
    assert response.status_code==201
    assert response.json()=={"message":"task created","task":{"id":1,"title":"add authentication","completed":False}}

def test_get_tasks(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response=client.get("/tasks")
    assert response.status_code==200
    assert response.json()==[{"id":task_id,"title":"test task","completed":False}]

def test_get_task(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response=client.get(f"/tasks/{task_id}")
    assert response.status_code==200
    assert response.json()=={"id":task_id,"title":"test task","completed":False}

def test_complete_task(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response= client.put(f"/tasks/{task_id}")
    assert response.status_code==200
    assert response.json()=={"id":task_id,"title":"test task","completed":True}

def test_delete_task(clean_tasks):
    create_response=client.post("/tasks",json={"title":"test task"})
    task_id=create_response.json()["task"]["id"]
    response= client.delete(f"/tasks/{task_id}")
    assert response.status_code==200
    assert response.json()=={"message":"task removed from the list"}

