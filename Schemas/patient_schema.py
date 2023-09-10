from pydantic import BaseModel

class PatientBase(BaseModel):
    patient_Name: str
    patient_age: int
    patient_address: str


class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_ID: int

    class Config:
        orm_mode = True
