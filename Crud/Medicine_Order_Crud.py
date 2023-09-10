from sqlalchemy.orm import Session
from models.medicine_Order import Medicine_Order as MedicineOrderModel
from Schemas.medicineOrder_schema import MedicineOrder
from Schemas.medicineOrder_schema import MedicineOrderCreate

# Read Operation
def get_medicine_order(db: Session, order_id: int):
    return db.query(MedicineOrderModel).filter(MedicineOrderModel.order_Id == order_id).first()

def get_medicine_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MedicineOrderModel).offset(skip).limit(limit).all()

# Create Operation
def create_medicine_order(db: Session, order: MedicineOrderCreate):
    db_order = MedicineOrderModel(medicinee_Id=order.medicinee_Id,patient_id=order.patient_Id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Delete Operation
def delete_medicine_order(db: Session, order_id: int):
    db_order = db.query(MedicineOrderModel).filter(MedicineOrderModel.order_Id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order

# Update Operation
def update_medicine_order(db: Session, order_id: int, order_data: MedicineOrderCreate):
    db_order = db.query(MedicineOrderModel).filter(MedicineOrderModel.order_Id == order_id).first()
    if db_order:
        # Update order attributes directly from order_data
        db_order.medicine_Id = order_data.medicinee_Id
       
        db.commit()
        db.refresh(db_order)
    return db_order
