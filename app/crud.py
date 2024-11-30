import httpx
from sqlalchemy.orm import Session
import models
import schemas


def get_warehouses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Warehouse).offset(skip).limit(limit).all()


def get_warehouse(db: Session, warehouse_id: int):
    return (
        db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()
    )


def create_warehouse(db: Session, warehouse: schemas.WarehouseCreate):
    db_warehouse = models.Warehouse(**warehouse.dict())
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse


def delete_warehouse(db: Session, warehouse_id: int):
    db_warehouse = (
        db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()
    )
    if db_warehouse:
        db.delete(db_warehouse)
        db.commit()
    return db_warehouse


# CRUD для товаров
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = (
        db.query(models.Product).filter(models.Product.id == product_id).first()
    )
    if db_product:
        # call order service
        product_name = db_product.name
        quantity = db_product.quantity
        warehouse_id = db_product.warehouse_id
        import asyncio

        asyncio.run(
            notify_order_service(product_id, product_name, quantity, warehouse_id)
        )

        # delete product
        db.delete(db_product)
        db.commit()
        return db_product
    return None


async def notify_order_service(
    product_id: int, product_name: str, quantity: int, location_id: int
):
    url = "http://orders_service:8000/orders"
    data = {
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "location_id": location_id,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        # TODO: process return
        response.raise_for_status()  # raise if status code not 2xx
        return response.json()
