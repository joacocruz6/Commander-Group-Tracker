from fastapi import APIRouter
from uuid import uuid4
router = APIRouter(prefix="/decks", tags=["decks"])

@router.post("/")
async def create_deck():
    person_id = str(uuid4())
    response = {
        "data": {
            "person_id": person_id
        }
    }
    return response

@router.get("/{deck_id}")
async def get_deck(deck_id: str):
    response = {
        "data": {
            "id": deck_id,
            "name": f"Deck {deck_id}"
        }
    }
    return response

@router.delete("/{deck_id}")
async def delete_deck(deck_id: str):
    response = {
        "data": {
            "id": deck_id,
            "message": f"Deck {deck_id} deleted successfully"
        }
    }
    return response