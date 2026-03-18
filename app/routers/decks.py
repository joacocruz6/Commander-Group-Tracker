from fastapi import APIRouter

router = APIRouter(prefix="/decks", tags=["decks"])

@router.post("/{person_id}")
async def create_deck(person_id: str):
    response = {
        "data": {
            "person_id": person_id
        }
    }
    return response

@router.get("/{person_id}")
async def list_person_decks(person_id: str):
    response = {
        "data": {
            "decks": [
                {
                    "id": "deck1",
                    "name": "Deck 1"
                },
                {
                    "id": "deck2",
                    "name": "Deck 2"
                }
            ]
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