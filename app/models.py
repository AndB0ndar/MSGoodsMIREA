from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)

    products = relationship("Product", back_populates="warehouse")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, default=1.0)
    quantity = Column(Integer, default=0)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))

    warehouse = relationship("Warehouse", back_populates="products")
