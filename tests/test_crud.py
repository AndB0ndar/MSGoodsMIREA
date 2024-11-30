from database import Base
from crud import create_product, get_product, delete_product
from schemas import ProductCreate


def test_create_product(db):
    product_data = ProductCreate(name="Test Product", price=100.0, quantity=10)
    product = create_product(db, product=product_data)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10


def test_get_product(db):
    product_data = ProductCreate(name="Test Product", price=100.0, quantity=10)
    product = create_product(db, product=product_data)
    fetched_product = get_product(db, product_id=product.id)
    assert fetched_product is not None
    assert fetched_product.name == "Test Product"

# TODO
def _test_delete_product(db):
    product_data = ProductCreate(name="Test Product", price=100.0, quantity=10)
    product = create_product(db, product=product_data)
    deleted_product = delete_product(db, product_id=product.id)
    assert deleted_product is not None
    assert deleted_product.name == "Test Product"

