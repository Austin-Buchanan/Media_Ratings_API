from pydantic import BaseModel, EmailStr
from datetime import datetime

# create schemas

class VideoGame(BaseModel):
    title: str
    platform: str
    developer: str
    rating: int

    class Config:
        orm_mode = True

class VideoGameOut(VideoGame):
    id: int
    title: str
    platform: str
    developer: str
    rating: int    
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str