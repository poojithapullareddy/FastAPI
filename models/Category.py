
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .Medicine import Medicine
from database import Base
from .Doctor import Doctor

class Category(Base):
    __tablename__ = "category"


    category_ID=Column(Integer,primary_key=True, index=True,autoincrement=True)
    category_Name=Column(String,nullable=False)
    category_image=Column(String,nullable=False)
    category_med= relationship("Medicine", back_populates="medicine")
    doctors = relationship('Doctor', back_populates='category')