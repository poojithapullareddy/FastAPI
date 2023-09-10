from pydantic import BaseModel
from .Doctor_Payment_schema import DoctorPayment
from typing import List

class DoctorAppointmentBase(BaseModel):
    patient_ID: int
    Doctor_Id: int
    Doctor_fee: int

class DoctorAppointmentCreate(DoctorAppointmentBase):
    pass

class DoctorAppointment(DoctorAppointmentBase):
    Appointment_Id: int
    appointment_doc:List[DoctorPayment]
    
    class Config:
        orm_mode = True
