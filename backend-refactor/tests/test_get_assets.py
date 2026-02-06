from fastapi.testclient import TestClient
from app.services.asset import AssetService

from app.main import app

client = TestClient(app)

def test_get_todo():

    response = client.get("api/v1/assets")

    assert response.status_code == 200
    assert response.json()[0]["asset_id"] == "1"

def test_get_nothing():

    class MockAsset:
        def get_all_assets(self):
            return []

    client.app.dependency_overrides[AssetService] = MockAsset

    response = client.get("api/v1/assets")

    assert response.status_code == 200
    assert response.json() == []
