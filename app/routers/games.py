from fastapi import APIRouter


router = APIRouter(prefix="/games", tags=["games"])

@router.post("/{playgroup_id}")
async def create_game(playgroup_id: str):
    response = {
        "data": {
            "playgroup_id": playgroup_id
        }
    }
    return response

@router.get("/{game_id}")
async def get_game(game_id: str):
    response = {
        "data": {
            "id": game_id,
            "name": f"Game {game_id}"
        }
    }
    return response

@router.put("/{game_id}")
async def update_game(game_id: str):
    response = {
        "data": {
            "id": game_id,
            "message": f"Game {game_id} updated successfully"
        }
    }
    return response

@router.get("/{playgroup_id}")
async def list_playgroup_games(playgroup_id: str):
    response = {
        "data": {
            "games": [
                {
                    "id": "game1",
                    "name": "Game 1"
                },
                {
                    "id": "game2",
                    "name": "Game 2"
                }
            ]
        }
    }
    return response