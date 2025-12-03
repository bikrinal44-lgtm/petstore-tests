import requests
import pytest

def test_create_pet(base_url, new_pet_data):
    """Тест POST /pet - создание нового питомца """

    response = requests.post(f"{base_url}/pet", json=new_pet_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_pet_data["id"]
    assert data["name"] == new_pet_data["name"]
    assert data["status"] == "available"

    delete_resp = requests.delete(f"{base_url}/pet/{new_pet_data['id']}")
    assert delete_resp.status_code in (200, 404)


def test_get_pet_by_id(base_url, new_pet_data):
    """Тест GET /pet/{petId} - получить питомца по ID """

    pet_id = new_pet_data["id"]
    response = requests.post(f"{base_url}/pet", json=new_pet_data)
    assert response.status_code == 200

    response = requests.get(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == pet_id
    assert data["name"] == new_pet_data["name"]
    assert data["status"] == "available"

    delete_resp = requests.delete(f"{base_url}/pet/{new_pet_data['id']}")
    assert delete_resp.status_code in (200, 404)


def test_get_pets_by_sold_status(base_url):
    """Тест GET /pet/findByStatus?status={status} со статусом 'sold' """

    status = "sold"
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    for pet in data:
        assert pet["status"] == status

def test_get_pets_by_pending_status(base_url):
    """Тест GET /pet/findByStatus?status={status} со статусом 'pending' """

    status = "pending"
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    for pet in data:
        assert pet["status"] == status

def test_get_pets_by_non_status(base_url):
    """Тест GET /pet/findByStatus?status={status} с несуществующим статусом """
    status = "non"
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    assert data == []

@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_get_pets_by_status(base_url, status):
    """ Тест GET /pet/findByStatus?status={status} со всеми существующими статусами статусом  """
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    for pet in data:
        assert pet["status"] == status

def test_get_pets_by_available_status(base_url):
    """Тест GET /pet/findByStatus?status={status} со статусом 'available' """
    status = "available"
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    for pet in data:
        assert pet["status"] == status


def test_update_pet_with_put(base_url, new_pet_data):
    """Тест PUT /pet - обновление данных питомца """
    requests.post(f"{base_url}/pet", json=new_pet_data)

    updated_data = new_pet_data.copy()
    updated_data["status"] = "sold"

    response = requests.put(f"{base_url}/pet", json=updated_data)
    assert response.status_code == 200

    resp = requests.get(f"{base_url}/pet/{new_pet_data['id']}")
    assert resp.json()["status"] == "sold"

    delete_resp = requests.delete(f"{base_url}/pet/{new_pet_data['id']}")
    assert delete_resp.status_code in (200, 404)  # 404 — если уже удалён

def test_delete_pet(base_url, new_pet_data):
    """Тест DELETE /pet/{petId} - удаление питомца """
    requests.post(f"{base_url}/pet", json=new_pet_data)

    response = requests.delete(f"{base_url}/pet/{new_pet_data['id']}")
    assert response.status_code == 200

    resp = requests.get(f"{base_url}/pet/{new_pet_data['id']}")
    assert resp.status_code == 404