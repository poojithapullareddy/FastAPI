from click import DateTime
from sqlalchemy import Column, ForeignKey, Integer,Boolean
from sqlalchemy.orm import relationship

from database import Base

class Medicinepayment(Base):
    __tablename__ = "MedicinePayment"

    medicinePayment_Id = Column(Integer, primary_key=True, index=True)
    # patient_Id = Column(Integer)
    status = Column(Boolean)
    order_Id = Column(Integer, ForeignKey("Medicine_Order.order_Id"))

    # Corrected relationship target class name and property name
    order = relationship("Medicine_Order", back_populates="Orderpay")
 
