from .database import engine, database
from . import models, posts

from fastapi import FastAPI

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router, prefix='', tags=['posts'])