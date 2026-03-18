import pytest
from fastapi.testclient import TestClient
from uuid import uuid4

class TestPersonsRouter:
    """Test suite for persons endpoints."""

    def test_create_person(self, client):
        """Test creating a new person in a playgroup."""
        data = {
            "name": "Test Person",
            "email": "cosme@fulanito.com"
        }
        response = client.post("/persons/", json=data)
        assert response.status_code == 200
        assert "data" in response.json()
        assert response.json()["data"]["name"] == data["name"]
        assert response.json()["data"]["email"] == data["email"]

    def test_get_person_details(self, client):
        """Test retrieving person details by ID."""
        person_id = str(uuid4())
        response = client.get(f"/persons/{person_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == person_id

    def test_update_person(self, client):
        """Test updating an existing person."""
        person_id = str(uuid4())
        data = {
            "name": "Updated Test Person",
        }
        response = client.put(f"/persons/{person_id}", json=data)
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == person_id

    def test_response_structure(self, client):
        """Test that all person endpoints follow the standard response wrapper format."""
        person_id = str(uuid4())
        response = client.get(f"/persons/{person_id}")
        assert isinstance(response.json(), dict)
        assert "data" in response.json()
