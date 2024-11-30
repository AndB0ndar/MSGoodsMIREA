from models import Product, Warehouse


def test_product_model():
    product = Product(name="Test Product", price=100.0, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10


def test_warehouse_model():
    warehouse = Warehouse(name="Test Warehouse", location="Test Location")
    assert warehouse.name == "Test Warehouse"
    assert warehouse.location == "Test Location"
