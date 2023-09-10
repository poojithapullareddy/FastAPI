from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Patient(Base):
    __tablename__ = "Patient"

    patient_ID = Column(Integer, primary_key=True, index=True)
    patient_Name = Column(String, nullable=False)
    patient_age = Column(Integer, nullable=False)
    patient_address = Column(String, nullable=False)
   
    
