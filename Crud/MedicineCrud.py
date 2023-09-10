from sqlalchemy.orm import Session
from models.Medicine import Medicine as MedicineModel
from Schemas.medicine_schema import MedicineCreate, Medicine

def get_medicine(db: Session, medicine_id: int):
    return db.query(MedicineModel).filter(MedicineModel.Medicine_ID == medicine_id).first()

def get_medicines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MedicineModel).offset(skip).limit(limit).all()

def create_medicine_order(db: Session, order: MedicineCreate):
    db_order = MedicineOrderModel(medicinee_Id=order.medicinee_Id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_medicine(db: Session, medicine_id: int):
    db_medicine = db.query(MedicineModel).filter(MedicineModel.Medicine_ID == medicine_id).first()
    if db_medicine:
        db.delete(db_medicine)
        db.commit()
    return db_medicine

def update_medicine(db: Session, medicine_id: int, medicine_data: MedicineCreate):
    db_medicine = db.query(MedicineModel).filter(MedicineModel.Medicine_ID == medicine_id).first()
    if db_medicine:
        db_medicine.Medicine_Name = medicine_data.Medicine_Name
        db_medicine.price = medicine_data.price
        db_medicine.quantity = medicine_data.quantity
        db_medicine.category_ID = medicine_data.category_ID

        db.commit()
        db.refresh(db_medicine)
    return db_medicine

