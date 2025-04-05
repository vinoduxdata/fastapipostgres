from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    brand_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    model_year = Column(Integer, nullable=False)
    list_price = Column(Float, nullable=False)