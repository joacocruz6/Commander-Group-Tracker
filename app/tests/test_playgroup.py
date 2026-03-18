import pytest
from fastapi.testclient import TestClient
from uuid import uuid4

class TestPlaygroupRouter:
    """Test suite for playgroup endpoints."""

    def test_create_playgroup(self, client):
        """Test creating a new playgroup."""
        data = {
            "name": "Cosme Fulanito's Playgroup",
        }
        response = client.post("/playgroups/", json=data)
        assert response.status_code == 200
        assert "data" in response.json()
        assert response.json()["data"]["name"] == "Cosme Fulanito's Playgroup"

    def test_get_playgroup_details(self, client):
        """Test retrieving playgroup details by ID."""
        playgroup_id = str(uuid4())
        response = client.get(f"/playgroups/{playgroup_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == playgroup_id

    def test_update_playgroup(self, client):
        """Test updating an existing playgroup."""
        playgroup_id = str(uuid4())
        updated_data = {
            "name": "Updated Playgroup Name"
        }
        response = client.put(f"/playgroups/{playgroup_id}", json=updated_data)
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == playgroup_id
        assert data["data"]["name"] == updated_data["name"]

    def test_get_user_created_playgroups(self, client):
        """Test retrieving playgroups created by the user."""
        response = client.get("/playgroups/admin")
        assert response.status_code == 200
        data = response.json()
        assert "playgroups" in data
        assert len(data["playgroups"]) == 2

    def test_get_user_playgroup_participant(self, client):
        """Test retrieving playgroups where user is a participant."""
        response = client.get("/playgroups/participant")
        # Endpoint raises HttpException(status_code=404)
        assert response.status_code == 404
