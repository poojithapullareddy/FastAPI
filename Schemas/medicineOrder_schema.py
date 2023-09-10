from pydantic import BaseModel


class MedicineOrderBase(BaseModel):
     medicinee_Id : int
     patient_Id :int

class MedicineOrderCreate(MedicineOrderBase):
    pass

class MedicineOrder(MedicineOrderBase):
    order_Id: int
    

    class Config:
        orm_mode = True
