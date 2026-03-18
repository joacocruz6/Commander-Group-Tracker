import pytest
from fastapi.testclient import TestClient


class TestDecksRouter:
    """Test suite for decks endpoints."""

    def test_create_deck(self, client):
        """Test creating a new deck."""
        response = client.post("/decks/")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "person_id" in data["data"]
        # person_id is generated server-side
        assert data["data"]["person_id"]

    def test_get_deck_details(self, client):
        """Test retrieving details of a specific deck."""
        deck_id = "deck-123"
        response = client.get(f"/decks/{deck_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == deck_id
        assert data["data"]["name"] == f"Deck {deck_id}"

    def test_delete_deck(self, client):
        """Test deleting a deck."""
        deck_id = "deck-999"
        response = client.delete(f"/decks/{deck_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == deck_id
        assert "message" in data["data"]
        assert f"Deck {deck_id} deleted successfully" in data["data"]["message"]

    def test_response_structure(self, client):
        """Test that all deck endpoints follow the standard response wrapper format."""
        response = client.post("/decks/")
        assert isinstance(response.json(), dict)
        assert "data" in response.json()
