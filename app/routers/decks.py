from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl
from uuid import uuid4
router = APIRouter(prefix="/decks", tags=["decks"])

class Deck(BaseModel):
    name: str
    commander: str
    deck_list_url: HttpUrl | None = None

@router.post("/")
async def create_deck(deck: Deck):
    deck_id = str(uuid4())
    response = {
        "data": {
            "id": deck_id,
            "name": deck.name,
            "commander": deck.commander,
            "deck_list_url": deck.deck_list_url
        }
    }
    return response

@router.get("/{deck_id}")
async def get_deck(deck_id: str):
    response = {
        "data": {
            "id": deck_id,
            "name": f"Deck {deck_id}",
            "commander": f"Commander for Deck {deck_id}",
            "deck_list_url": f"https://example.com/decks/{deck_id}/list"
        }
    }
    return response

@router.put("/{deck_id}")
async def update_deck(deck_id: str, deck: Deck):
    response = {
        "data": {
            "id": deck_id,
            "name": deck.name,
            "commander": deck.commander,
            "deck_list_url": deck.deck_list_url
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