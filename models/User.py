from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "User"

    User_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    user_Name = Column(String)
    password = Column(String)
    phone_Number = Column(Integer)
    created_By = Column(String)
    created_On = Column(DateTime, default=datetime.utcnow)
    updated_By = Column(String)
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    role = Column(String)
