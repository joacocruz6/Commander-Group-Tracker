from fastapi import APIRouter


router = APIRouter(prefix="/games", tags=["games"])

@router.post("/")
async def create_game():
    playgroup_id = str(uuid4())
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