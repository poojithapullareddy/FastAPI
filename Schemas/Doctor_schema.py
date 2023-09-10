from pydantic import BaseModel

class DoctorBase(BaseModel):
    doctor_Name: str
    doctor_experience: int
    contact_Info: int
    hospital_Address: str
    category_id:int
class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    doctor_ID: int

    class Config:
        orm_mode = True
