from database import engine, Base
from models.db_models import Task
Base.metadata.create_all(bind=engine)