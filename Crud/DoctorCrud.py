from sqlalchemy.orm import Session
from models.Patient import Patient as PatientModel
from Schemas.patient_schema import PatientCreate, Patient

def get_patient(db: Session, patient_id: int):
    return db.query(PatientModel).filter(PatientModel.patient_ID == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PatientModel).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: PatientCreate):
    db_patient = PatientModel(
        patient_Name=patient.patient_Name,
        patient_age=patient.patient_age,
        patient_address=patient.patient_address
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(PatientModel).filter(PatientModel.patient_ID == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient

def update_patient(db: Session, patient_id: int, patient_data: PatientCreate):
    db_patient = db.query(PatientModel).filter(PatientModel.patient_ID == patient_id).first()
    if db_patient:
        db_patient.patient_Name = patient_data.patient_Name
        db_patient.patient_age = patient_data.patient_age
        db_patient.patient_address = patient_data.patient_address

        db.commit()
        db.refresh(db_patient)
    return db_patient
