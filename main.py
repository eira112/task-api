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

@app.get("/")
def root():
    return {"message": "Task API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(task_router)