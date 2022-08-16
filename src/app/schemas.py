from pydantic import BaseModel

class PostBase(BaseModel):
    url: str
    created_by: str
    text: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    

    class Config:
        orm_mode = True