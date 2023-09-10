from sqlalchemy.orm import Session,selectinload
from models.DoctorAppointment import DoctorAppointment as DoctorAppointmentModel
from Schemas.DoctorAppointment_schema import DoctorAppointment
from Schemas.DoctorAppointment_schema import DoctorAppointmentCreate

# Read Operation
def get_doctor_appointment(db: Session, appointment_id: int):
    return db.query(DoctorAppointmentModel).filter(DoctorAppointmentModel.Appointment_Id == appointment_id).first()

def get_doctor_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DoctorAppointmentModel).offset(skip).limit(limit).options(selectinload(DoctorAppointment.appointment_doc)).all()

# Create Operation
def create_doctor_appointment(db: Session, appointment: DoctorAppointmentCreate):
    db_appointment = DoctorAppointmentModel(
        patient_ID=appointment.patient_ID,
        Doctor_Id=appointment.Doctor_Id,
        Doctor_fee=appointment.Doctor_fee
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# Delete Operation
def delete_doctor_appointment(db: Session, appointment_id: int):
    db_appointment = db.query(DoctorAppointmentModel).filter(DoctorAppointmentModel.Appointment_Id == appointment_id).first()
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
    return db_appointment

# Update Operation
def update_doctor_appointment(db: Session, appointment_id: int, appointment_data: DoctorAppointmentCreate):
    db_appointment = db.query(DoctorAppointmentModel).filter(DoctorAppointmentModel.Appointment_Id == appointment_id).first()
    if db_appointment:
        # Update appointment attributes directly from appointment_data
        db_appointment.patient_ID = appointment_data.patient_ID
        db_appointment.Doctor_Id = appointment_data.Doctor_Id
        db_appointment.Doctor_fee = appointment_data.Doctor_fee

        db.commit()
        db.refresh(db_appointment)
    return db_appointment
