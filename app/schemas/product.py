from pydantic import BaseModel

class ProductBase(BaseModel):
    product_name: str
    brand_id: int
    category_id: int
    model_year: int
    list_price: float

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
