from click import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Medicine(Base):
    __tablename__ = "Medicine"
    Medicine_ID = Column(Integer, primary_key=True)
    Medicine_Name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(String, nullable=False)
    category_ID = Column(Integer,ForeignKey("category.category_ID"))
    
    medicine = relationship("Category", back_populates="category_med")
