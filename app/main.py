from fastapi import FastAPI
from app.api.v1 import product
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Products API")

app.include_router(product.router, prefix="/api/v1/products", tags=["Products"])