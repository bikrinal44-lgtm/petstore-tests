import pytest
import uuid

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def new_pet_data():
    unique_id = int(str(uuid.uuid4().int)[:9])
    return {
        "id": unique_id,
        "name": f"Name",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["string"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }

@pytest.fixture
def new_order_data():
    unique_id = int(str(uuid.uuid4().int)[:9])
    return {
        "id": unique_id,
        "petId": 11111,
        "quantity": 1,
        "shipDate": "2025-12-02T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }