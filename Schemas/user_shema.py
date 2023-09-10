from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    user_Name: str
    password: str
    phone_Number: int
    
    role: str

class UserCreate(UserBase):
    created_By: str
    created_On: datetime
    updated_By: str
    updated_on: datetime

class User(UserBase):
    User_id: int
    __module__

    class Config:
        orm_mode = True
        __module__
       
