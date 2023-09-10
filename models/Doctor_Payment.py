from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database import Base
class DoctorPayment(Base):
    __tablename__ = "DoctorPayment"

    payment_ID=Column(Integer,primary_key=True,index=True,autoincrement=True)
    Appointment = Column(Integer, ForeignKey("DoctorAppointment.Appointment_Id"))
    doctor_app = relationship("DoctorAppointment", back_populates="appointment_doc")