from pydantic import BaseModel

class MedicineBase(BaseModel):
    Medicine_Name: str
    price: int
    quantity: str
    category_ID: int

class MedicineCreate(MedicineBase):
    pass

class Medicine(MedicineBase):
    Medicine_ID: int

    class Config:
        orm_mode = True
