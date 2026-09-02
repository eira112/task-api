from fastapi import FastAPI
from routes.task_routes import router as task_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)


@app.get("/")
def home():
    return {"message": "task api is running"}