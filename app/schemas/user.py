from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    role: str  # 'donator' or 'organisation'

class UserCreate(UserBase):
    password: str  # raw password when user signs up

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
