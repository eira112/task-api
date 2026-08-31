from fastapi import FastAPI
from routes.task_routes import router as task_router

app = FastAPI()

app.include_router(task_router)


@app.get("/")
def home():
    return {"message": "task api is running"}