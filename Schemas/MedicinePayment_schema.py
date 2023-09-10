from pydantic import BaseModel

class MedicinePaymentBase(BaseModel):
    patient_Id: int
    status: bool
    order_Id: int

class MedicinePaymentCreate(MedicinePaymentBase):
    pass

class MedicinePayment(MedicinePaymentBase):
    medicinePayment_Id: int

    class Config:
        orm_mode = True
