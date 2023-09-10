from sqlalchemy.orm import Session
from models.Medicinepayment import Medicinepayment as MedicinePaymentModel
from Schemas.MedicinePayment_schema import  MedicinePayment
from Schemas.MedicinePayment_schema import MedicinePaymentCreate
from models.medicine_Order import Medicine_Order
# Read Operation
def get_medicine_payment(db: Session, payment_id: int):
    return db.query(MedicinePaymentModel).filter(MedicinePaymentModel.medicinePayment_Id == payment_id).first()

def get_medicine_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MedicinePaymentModel).offset(skip).limit(limit).all()

def create_medicine_payment(db: Session, payment: MedicinePaymentCreate):
    db_payment = MedicinePaymentModel(status=payment.status, order_Id=payment.order_Id)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment





# Delete Operation
def delete_medicine_payment(db: Session, payment_id: int):
    db_payment = db.query(MedicinePaymentModel).filter(MedicinePaymentModel.medicinePayment_Id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment

# Update Operation
def update_medicine_payment(db: Session, payment_id: int, payment_data: MedicinePaymentCreate):
    db_payment = db.query(MedicinePaymentModel).filter(MedicinePaymentModel.medicinePayment_Id == payment_id).first()
    if db_payment:
        # Update payment attributes directly from payment_data
        db_payment.patient_Id = payment_data.patient_Id
        db_payment.status = payment_data.status
        db_payment.order_Id = payment_data.order_Id
       
        db.commit()
        db.refresh(db_payment)
    return db_payment
