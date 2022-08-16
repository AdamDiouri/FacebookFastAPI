from .database import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    text = Column(String)
    created_by = Column(String)