from sqlalchemy.orm import Session
from models.User import User as UserModel
from Schemas.user_shema import UserCreate
from Schemas.user_shema import User
def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.User_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        email=user.email,
        user_Name=user.user_Name,
        password=user.password,
        phone_Number=user.phone_Number,
        created_By=user.created_By,
        created_On=user.created_On,
        updated_By=user.updated_By,
        updated_on=user.updated_on,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(UserModel).filter(UserModel.User_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def update_user(db: Session, user_id: int, user_data: UserCreate):
    db_user = db.query(UserModel).filter(UserModel.User_id == user_id).first()
    if db_user:
        db_user.email = user_data.email
        db_user.user_Name = user_data.user_Name
        db_user.password = user_data.password
        db_user.phone_Number = user_data.phone_Number
        db_user.created_By = user_data.created_By
        db_user.created_On = user_data.created_On
        db_user.updated_By = user_data.updated_By
        db_user.updated_on = user_data.updated_on
        db_user.role = user_data.role

        db.commit()
        db.refresh(db_user)
    return db_user
