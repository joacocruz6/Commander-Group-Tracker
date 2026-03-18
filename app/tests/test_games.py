import pytest
from fastapi.testclient import TestClient
from uuid import uuid4

class TestGamesRouter:
    """Test suite for games endpoints."""

    def test_create_game(self, client):
        """Test creating a new game result."""
        response = client.post("/games/")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "playgroup_id" in data["data"]
        # playgroup_id is generated server-side
        assert data["data"]["playgroup_id"]

    def test_get_game_details(self, client):
        """Test retrieving details of a specific game."""
        game_id = str(uuid4())
        response = client.get(f"/games/{game_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == game_id
        assert data["data"]["name"] == f"Game {game_id}"

    def test_update_game(self, client):
        """Test updating an existing game."""
        game_id = str(uuid4())
        response = client.put(f"/games/{game_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == game_id
        assert "message" in data["data"]

    def test_response_structure(self, client):
        """Test that all game endpoints follow the standard response wrapper format."""
        response = client.post("/games/")
        assert isinstance(response.json(), dict)
        assert "data" in response.json()
