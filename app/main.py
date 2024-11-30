from fastapi import FastAPI
from routers import warehouses, products
from database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(warehouses.router, prefix="/warehouses", tags=["warehouses"])
app.include_router(products.router, prefix="/products", tags=["products"])
