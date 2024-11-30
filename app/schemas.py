from pydantic import BaseModel
from typing import List, Optional


class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    warehouse_id: Optional[int] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class WarehouseBase(BaseModel):
    name: str
    location: str


class WarehouseCreate(WarehouseBase):
    pass


class Warehouse(WarehouseBase):
    id: int
    products: List[Product] = []

    class Config:
        orm_mode = True
