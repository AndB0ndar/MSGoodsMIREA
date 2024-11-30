def test_read_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_product(client):
    product_data = {"name": "Test Product", "price": 100.0, "quantity": 10}
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 100.0
    assert data["quantity"] == 10


def test_get_product(client):
    product_data = {"name": "Test Product", "price": 100.0, "quantity": 10}
    post_response = client.post("/products/", json=product_data)
    assert post_response.status_code == 200
    product_id = post_response.json()["id"]

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Product"


# TODO
def _test_delete_product(client):
    product_data = {"name": "Test Product", "price": 100.0, "quantity": 10}
    post_response = client.post("/products/", json=product_data)
    assert post_response.status_code == 200
    product_id = post_response.json()["id"]

    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["name"] == "Test Product"

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404
