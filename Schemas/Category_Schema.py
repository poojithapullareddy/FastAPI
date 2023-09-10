from pydantic import BaseModel

class CategoryBase(BaseModel):
    category_Name: str
    category_image: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    category_ID: int

    class Config:
        orm_mode = True
