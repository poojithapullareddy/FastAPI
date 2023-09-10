from pydantic import BaseModel

class DoctorPaymentBase(BaseModel):
    Appointment: int

class DoctorPaymentCreate(DoctorPaymentBase):
    pass

class DoctorPayment(DoctorPaymentBase):
    payment_ID: int

    class Config:
        orm_mode = True
