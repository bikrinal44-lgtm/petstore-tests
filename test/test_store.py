import requests


def test_get_inventory(base_url):
    """Тест GET /store/inventory - получить инвентарь"""

    response = requests.get(f"{base_url}/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_create_order(base_url, new_order_data):
    """Тест POST /store/order - создание заказа"""

    response = requests.post(f"{base_url}/store/order", json=new_order_data)
    assert response.status_code == 200
    created = response.json()

    assert created["id"] == new_order_data["id"]
    assert created["petId"] == new_order_data["petId"]
    assert created["status"] == new_order_data["status"]


def test_delete_order(base_url, new_order_data):
    """Тест DELETE /store/order/{orderId} - удаление заказа"""

    create_resp = requests.post(f"{base_url}/store/order", json=new_order_data)
    assert create_resp.status_code == 200

    order_id = new_order_data["id"]

    delete_resp = requests.delete(f"{base_url}/store/order/{order_id}")
    assert delete_resp.status_code == 200

    get_resp = requests.get(f"{base_url}/store/order/{order_id}")
    assert get_resp.status_code in (404, 500)