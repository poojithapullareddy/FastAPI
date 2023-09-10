from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .Doctor_Payment import DoctorPayment
from database import Base
class DoctorAppointment(Base):
    __tablename__ = "DoctorAppointment"

    Appointment_Id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    patient_ID=Column(Integer)
    Doctor_Id=Column(Integer)
    Doctor_fee=Column(Integer)
    appointment_doc=relationship("DoctorPayment",back_populates="doctor_app",lazy="selectin")
    