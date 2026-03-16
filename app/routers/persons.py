from fastapi import APIRouter

router = APIRouter(prefix='/persons', tag=['persons'])

@router.post("/")
async def create_new_person():
    response = {
        "data": "Hello World!"
    }
    return response

@router.get("/{person_id}")
async def get_person_details(person_id: str):
    response = {
        "data": {
            "id": person_id
        }
    }
    return response

@router.put("/{person_id}")
async def put_person(person_id: str):
    response = {
        "data": {
            "id": person_id
        }
    }
    return response