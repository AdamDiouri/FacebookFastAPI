from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from facebook_scraper import get_posts
from . import crud, models, schemas
from .database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/posts/', response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip=skip, limit=limit)


@router.get('/posts/{post_id}',response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post Not Found')
    else:
        return db_post


@router.get('/posts/populate/', response_model=list[schemas.Post])
def populate_database(db: Session = Depends(get_db)):
    for p in get_posts('nintendo', pages=10):
        post = {
            'url': '' if p['post_url'] is None else p['post_url'],
            'created_by': '' if p['username'] is None else p['username'],
            'text': '' if p['text'] is None else p['text'] 
        }
        db_post = schemas.PostCreate(url=post['url'], created_by=post['created_by'], text=post['text'])
        crud.create_post(db=db, post=db_post)
    return crud.get_posts(db)