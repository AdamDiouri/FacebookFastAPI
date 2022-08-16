from sqlalchemy.orm import Session
from . import models, schemas

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(created_by=post.created_by, url=post.created_by, text=post.text)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)