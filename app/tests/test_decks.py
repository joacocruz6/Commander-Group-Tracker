import pytest
from fastapi.testclient import TestClient
from uuid import uuid4


class TestDecksRouter:
    """Test suite for decks endpoints."""

    def test_create_deck(self, client):
        """Test creating a new deck."""
        deck_data = {
            "name": "Test Deck",
            "commander": "Test Commander",
            "deck_list_url": "https://example.com/decks/test-deck/list"
        }
        response = client.post("/decks/", json=deck_data)
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "id" in data["data"]
        # deck_id is generated server-side
        assert data["data"]["id"]

    def test_get_deck_details(self, client):
        """Test retrieving details of a specific deck."""
        deck_id = str(uuid4())
        response = client.get(f"/decks/{deck_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == deck_id
        assert data["data"]["name"] == f"Deck {deck_id}"
        assert data["data"]["commander"] == f"Commander for Deck {deck_id}"
        assert data["data"]["deck_list_url"] == f"https://example.com/decks/{deck_id}/list"

    def test_update_deck(self, client):
        """Test updating an existing deck."""
        deck_id = str(uuid4())
        updated_deck_data = {
            "name": "Updated Test Deck",
            "commander": "Updated Test Commander",
            "deck_list_url": "https://example.com/decks/updated-test-deck/list"
        }
        response = client.put(f"/decks/{deck_id}", json=updated_deck_data)
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == deck_id
        assert data["data"]["name"] == updated_deck_data["name"]
        assert data["data"]["commander"] == updated_deck_data["commander"]
        assert data["data"]["deck_list_url"] == updated_deck_data["deck_list_url"]

    def test_delete_deck(self, client):
        """Test deleting a deck."""
        deck_id = str(uuid4())
        response = client.delete(f"/decks/{deck_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == deck_id
        assert "message" in data["data"]
        assert f"Deck {deck_id} deleted successfully" in data["data"]["message"]

    def test_response_structure(self, client):
        """Test that all deck endpoints follow the standard response wrapper format."""
        deck_data = {
            "name": "Test Deck",
            "commander": "Test Commander",
            "deck_list_url": "https://example.com/decks/test-deck/list"
        }
        response = client.post("/decks/", json=deck_data)
        assert isinstance(response.json(), dict)
        assert "data" in response.json()
