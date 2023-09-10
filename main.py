from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models.User import User as UserModel
from Schemas.user_shema import UserCreate
from Schemas.user_shema import User
from Crud import UserCrud
from database import Base
from database import SessionLocal, engine
from models.DoctorAppointment import DoctorAppointment as DoctorAppointmentModel
from Schemas.DoctorAppointment_schema import DoctorAppointment
from Schemas.DoctorAppointment_schema import DoctorAppointmentCreate
from Crud import DoctorAppointmentCrud

from models.medicine_Order import Medicine_Order as MedicineOrderModel
from Schemas.medicineOrder_schema import MedicineOrder
from Schemas.medicineOrder_schema import MedicineOrderCreate
from Crud import Medicine_Order_Crud as crud
from Crud import UserCrud
from Crud import CategoryCrud
from Crud import MedicineCrud
from Crud import DoctorCrud
from Crud import PatientCrud
from Schemas.patient_schema import Patient,PatientCreate
from Schemas.Category_Schema import Category
from Schemas.Doctor_schema import  Doctor
from Schemas.Category_Schema import CategoryCreate
from Schemas.medicine_schema import Medicine
from Schemas.medicine_schema import MedicineCreate
from Schemas.Doctor_schema import DoctorCreate


from Schemas.MedicinePayment_schema import MedicinePayment
from Schemas.MedicinePayment_schema import MedicinePaymentCreate
from Crud import medicine_Payment_Crud 

from models.Doctor_Payment import DoctorPayment as DoctorPaymentModel
from Schemas.Doctor_Payment_schema import DoctorPayment 
from Schemas.Doctor_Payment_schema import DoctorPaymentCreate
from Crud import Doctor_Payment_Crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#------------------------------------category- sucess------------------------
@app.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = CategoryCrud.get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.get("/categories/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = CategoryCrud.get_categories(db, skip, limit)
    return categories



@app.post("/categories/", response_model=Category)
def create_category(category:Category, db: Session = Depends(get_db)):
    return CategoryCrud.create_category(db, category)


@app.delete("/categories/{category_id}", response_model=Category)
def delete_user12(category_id: int, db: Session = Depends(get_db)):
    db_user = CategoryCrud.delete_category(db=db, category_id=category_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="category not found")
    return db_user


@app.put("/categories/{category_id}", response_model=Category)
def update_category_endpoint(
    category_id: int,
    category_data:CategoryCreate,
    db: Session = Depends(get_db)
):
    db_category = CategoryCrud.update_category(db, category_id, category_data)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return db_category

#==============================================================================================

#+++++++++++++++++++++++++++++MEDICINE-SUCCESS++++++++++++++++++++++++++++++++++++++

@app.post("/medicines/", response_model=Medicine)
def create_medicine(medicine:Medicine, db: Session = Depends(get_db)):
     return MedicineCrud.create_medicine(db, medicine)
@app.get("/medicines/{medicine_id}", response_model=Medicine)
def read_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine =  Medicidicines


@app.put("/medicines/{medicine_id}", response_model=Medicine)
def update_medicine_endpoint(
    medicine_id: int,
    medicine_data: MedicineCreate,
    db: Session = Depends(get_db)
):
    db_medicine =  MedicineCrud.update_medicine(db, medicine_id, medicine_data)
    if db_medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return db_medicine

@app.delete("/medicines/{medicine_id}", response_model=Medicine)
def delete_medicine_endpoint(medicine_id: int, db: Session = Depends(get_db)):
    db_medicine =  MedicineCrud.delete_medicine(db, medicine_id)
    if db_medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return db_medicineneCrud.get_medicine(db, medicine_id)
    if medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine


@app.get("/medicines/", response_model=list[Medicine])
def read_medicines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medicines = MedicineCrud.get_medicines(db, skip, limit)
    return medicines
#------------------------------------------------------------------------------------------------------------
#+++++++++++++++++++++++++++++++++++++++++++++++++Doctor Success+++++++++++++++++++++++++++++++++++++++

@app.get("/doctors/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = DoctorCrud.get_doctor(db, doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.get("/doctors/", response_model=list[Doctor])
def read_medicines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medicines = DoctorCrud.get_doctors(db, skip, limit)
    return medicines

@app.post("/doctors/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    return DoctorCrud.create_doctor(db, doctor)


@app.put("/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(
    doctor_id: int,
    doctor_data: DoctorCreate,
    db: Session = Depends(get_db)
):
    db_doctor = DoctorCrud.update_doctor(db, doctor_id, doctor_data)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@app.delete("/doctors/{doctor_id}", response_model=Doctor)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = DoctorCrud.delete_doctor(db, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#+++++++++++++++++++++++++++++++++++++PATIENT-SUCCESS+++++++++++++++++++

@app.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = PatientCrud.get_patient(db, patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.get("/patients/", response_model=list[Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = PatientCrud.get_patients(db, skip, limit)
    return patients

@app.post("/patients/", response_model=Patient)
def create_patient_endpoint(patient: PatientCreate, db: Session = Depends(get_db)):
    return PatientCrud.create_patient(db, patient)

@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient_endpoint(
    patient_id: int,
    patient_data: PatientCreate,
    db: Session = Depends(get_db)
):
    db_patient =PatientCrud.update_patient(db, patient_id, patient_data)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.delete("/patients/{patient_id}", response_model=Patient)
def delete_patient_endpoint(patient_id: int, db: Session = Depends(get_db)):
    db_patient = PatientCrud.delete_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#____________________________________________medicine-order SUCESS___________________

@app.get("/medicine_orders/{order_id}", response_model=MedicineOrder)
def read_medicine_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_medicine_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Medicine Order not found")
    return order

@app.get("/medicine_orders/", response_model=list[MedicineOrder])
def read_medicine_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_medicine_orders(db, skip, limit)
    return orders


@app.post("/medicine_orders/", response_model=MedicineOrder)
def create_medicine_order_endpoint(order: MedicineOrderCreate, db: Session = Depends(get_db)):
    return  crud.create_medicine_order(db, order)

@app.put("/medicine_orders/{order_id}", response_model=MedicineOrder)
def update_medicine_order_endpoint(order_id: int, order_data: MedicineOrderCreate, db: Session = Depends(get_db)):
    db_order =crud.update_medicine_order(db, order_id, order_data)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Medicine Order not found")
    return db_order


@app.delete("/medicine_orders/{order_id}", response_model=MedicineOrder)
def delete_medicine_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order =  crud.delete_medicine_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Medicine Order not found")
    return db_order

#************************************************PAYMENT ORDER SUCCESS******************

@app.get("/medicine_payments/{payment_id}", response_model=MedicinePayment)
def read_medicine_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = medicine_Payment_Crud .get_medicine_payment(db, payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Medicine Payment not found")
    return payment

@app.get("/medicine_payments/", response_model=list[MedicinePayment])
def read_medicine_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments =medicine_Payment_Crud . get_medicine_payments(db, skip, limit)
    return payments

@app.post("/medicine_payments/", response_model=MedicinePayment)
def create_medicine_payment_endpoint(payment: MedicinePaymentCreate, db: Session = Depends(get_db)):
    return medicine_Payment_Crud .create_medicine_payment(db, payment)

@app.put("/medicine_payments/{payment_id}", response_model=MedicinePayment)
def update_medicine_payment_endpoint(payment_id: int, payment_data: MedicinePaymentCreate, db: Session = Depends(get_db)):
    db_payment = medicine_Payment_Crud .update_medicine_payment(db, payment_id, payment_data)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Medicine Payment not found")
    return db_payment

@app.delete("/medicine_payments/{payment_id}", response_model=MedicinePayment)
def delete_medicine_payment_endpoint(payment_id: int, db: Session = Depends(get_db)):
    db_payment = medicine_Payment_Crud .delete_medicine_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Medicine Payment not found")
    return db_payment
#***************************************************************************
#-------------------------Doctor-Appointment Success-----------------------------
@app.get("/doctor_appointments/{appointment_id}", response_model=DoctorAppointment)
def read_doctor_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = DoctorAppointmentCrud.get_doctor_appointment(db, appointment_id)
    if appointment is None:
        raise HTTPException(status_code=404, detail="Doctor Appointment not found")
    return appointment

@app.get("/doctor_appointments/", response_model=list[DoctorAppointment])
def read_doctor_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = DoctorAppointmentCrud.get_doctor_appointments(db, skip, limit)
    return appointments

@app.post("/doctor_appointments/", response_model=DoctorAppointment)
def create_doctor_appointment_endpoint(appointment: DoctorAppointmentCreate, db: Session = Depends(get_db)):
    return DoctorAppointmentCrud.create_doctor_appointment(db, appointment)

@app.put("/doctor_appointments/{appointment_id}", response_model=DoctorAppointment)
def update_doctor_appointment_endpoint(appointment_id: int, appointment_data: DoctorAppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = DoctorAppointmentCrud.update_doctor_appointment(db, appointment_id, appointment_data)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Doctor Appointment not found")
    return db_appointment

@app.delete("/doctor_appointments/{appointment_id}", response_model=DoctorAppointment)
def delete_doctor_appointment_endpoint(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = DoctorAppointmentCrud.delete_doctor_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Doctor Appointment not found")
    return db_appointment


@app.post("/doctor_payments/", response_model=DoctorPayment)
def create_doctor_payment_endpoint(payment: DoctorPaymentCreate, db: Session = Depends(get_db)):
    return Doctor_Payment_Crud.create_doctor_payment(db, payment)

# Get a Doctor Payment by ID
@app.get("/doctor_payments/{payment_id}", response_model=DoctorPayment)
def read_doctor_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = Doctor_Payment_Crud.get_doctor_payment(db, payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Doctor Payment not found")
    return payment

# Get all Doctor Payments
@app.get("/doctor_payments/", response_model=list[DoctorPayment])
def read_doctor_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments =Doctor_Payment_Crud. get_doctor_payments(db, skip, limit)
    return payments

# Update a Doctor Payment by ID
@app.put("/doctor_payments/{payment_id}", response_model=DoctorPayment)
def update_doctor_payment_endpoint(payment_id: int, payment_data: DoctorPaymentCreate, db: Session = Depends(get_db)):
    db_payment = Doctor_Payment_Crud.update_doctor_payment(db, payment_id, payment_data)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Doctor Payment not found")
    return db_payment

# Delete a Doctor Payment by ID
@app.delete("/doctor_payments/{payment_id}", response_model=DoctorPayment)
def delete_doctor_payment_endpoint(payment_id: int, db: Session = Depends(get_db)):
    db_payment = Doctor_Payment_Crud.delete_doctor_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Doctor Payment not found")
    return db_payment
#-------------------------------------------------------------------------------------------


# Create User
@app.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return UserCrud.create_user(db, user)

# Read User by ID
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserCrud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# # Read Users (with pagination)
@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return UserCrud.get_users(db, skip, limit)

# Update User by ID
@app.put("/users/{user_id}", response_model=User)
def update_user_endpoint(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    db_user = UserCrud.update_user(db, user_id, user_data)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete User by ID
@app.delete("/users/{user_id}", response_model=User)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user =UserCrud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user