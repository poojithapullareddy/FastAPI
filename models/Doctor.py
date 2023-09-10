from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Doctor(Base):
    __tablename__ = "Doctor"
    doctor_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doctor_Name = Column(String)
    doctor_experience = Column(Integer)
    contact_Info = Column(Integer)
    hospital_Address = Column(String)
    category_id = Column(Integer, ForeignKey("category.category_ID"))
    category = relationship('Category', back_populates='doctors')
    