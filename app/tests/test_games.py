import pytest
from fastapi.testclient import TestClient


class TestGamesRouter:
    """Test suite for games endpoints.
    
    Note: The games router has overlapping GET endpoints.
    Both GET endpoints use /{id}, which creates routing ambiguity.
    These tests assume path differentiation based on ID format or request context.
    """

    def test_create_game(self, client):
        """Test creating a new game result for a playgroup."""
        playgroup_id = "group-123"
        response = client.post(f"/games/{playgroup_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["playgroup_id"] == playgroup_id

    def test_get_game_details(self, client):
        """Test retrieving details of a specific game."""
        game_id = "game-456"
        response = client.get(f"/games/{game_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == game_id
        assert data["data"]["name"] == f"Game {game_id}"

    def test_update_game(self, client):
        """Test updating an existing game."""
        game_id = "game-789"
        response = client.put(f"/games/{game_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == game_id
        assert "message" in data["data"]

    def test_list_playgroup_games(self, client):
        """Test listing all games for a specific playgroup.
        
        NOTE: This endpoint has a ROUTING CONFLICT with get_game().
        Both use GET /{id}, so they cannot coexist with current routing.
        Currently, get_game() matches first and returns a single game.
        This test documents the current behavior.
        
        To resolve: Refactor to use /playgroup/{playgroup_id}/games
        or add a query parameter like ?list=true.
        """
        playgroup_id = "group-999"
        response = client.get(f"/games/{playgroup_id}")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        # Currently matches get_game() endpoint, not list_playgroup_games()
        assert "id" in data["data"]  # This is from get_game()

    def test_response_structure(self, client):
        """Test that all game endpoints follow the standard response wrapper format."""
        playgroup_id = "group-123"
        response = client.post(f"/games/{playgroup_id}")
        assert isinstance(response.json(), dict)
        assert "data" in response.json()
