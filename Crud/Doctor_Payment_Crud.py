from sqlalchemy.orm import Session
from models.Doctor_Payment import DoctorPayment as DoctorPaymentModel
from Schemas.Doctor_Payment_schema import DoctorPayment
from Schemas.Doctor_Payment_schema import DoctorPaymentCreate

# Create Operation
def create_doctor_payment(db: Session, payment: DoctorPaymentCreate):
    db_payment = DoctorPaymentModel(Appointment=payment.Appointment)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

# Read Operation
def get_doctor_payment(db: Session, payment_id: int):
    return db.query(DoctorPaymentModel).filter(DoctorPaymentModel.payment_ID == payment_id).first()

def get_doctor_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DoctorPaymentModel).offset(skip).limit(limit).all()

# Update Operation
def update_doctor_payment(db: Session, payment_id: int, payment_data: DoctorPaymentCreate):
    db_payment = db.query(DoctorPaymentModel).filter(DoctorPaymentModel.payment_ID == payment_id).first()
    if db_payment:
        # Update payment attributes directly from payment_data
        db_payment.Appointment = payment_data.Appointment
        db.commit()
        db.refresh(db_payment)
    return db_payment

# Delete Operation
def delete_doctor_payment(db: Session, payment_id: int):
    db_payment = db.query(DoctorPaymentModel).filter(DoctorPaymentModel.payment_ID == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment
