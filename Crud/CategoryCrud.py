from sqlalchemy.orm import Session



from sqlalchemy.orm import Session
from  models.Category import Category as CategoryModel
from  Schemas.Category_Schema import Category
from  Schemas.Category_Schema import CategoryCreate


def get_category(db: Session, category_id: int):
    return db.query(CategoryModel).filter(CategoryModel.category_ID == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryModel).offset(skip).limit(limit).all()

# Create Operation
def create_category(db
: Session, category: Category):
    db_category = CategoryModel(category_Name=category.category_Name, category_image=category.category_image)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category



def delete_category(db: Session, category_id: int):
    db_category = db.query(CategoryModel).filter(CategoryModel.category_ID == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

def update_category(db: Session, category_id: int, category_data: CategoryCreate):
    db_category = db.query(CategoryModel).filter(CategoryModel.category_ID == category_id).first()
    if db_category:
        # Update category attributes directly from category_data
        db_category.category_Name = category_data.category_Name
        db_category.category_image = category_data.category_image

        db.commit()
        db.refresh(db_category)
    return db_category
