from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .Medicinepayment import Medicinepayment
from database import Base

class Medicine_Order(Base):
    __tablename__ = "Medicine_Order"
    order_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    medicinee_Id = Column(Integer)
    patient_Id = Column(Integer)
    Orderpay = relationship("Medicinepayment", back_populates="order",lazy="selectin")
