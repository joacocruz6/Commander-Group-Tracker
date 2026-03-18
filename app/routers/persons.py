from fastapi import APIRouter
from uuid import uuid4
from pydantic import BaseModel, EmailStr
router = APIRouter(prefix='/persons', tags=['persons'])

class Person(BaseModel):
    name: str
    email: EmailStr | None = None

@router.post("/")
async def create_new_person(person: Person):
    uuid = str(uuid4())
    name = person.name
    email = person.email
    response = {
        "data": {
            "id": uuid,
            "name": name,
            "email": email
        }
    }
    return response

@router.get("/{person_id}")
async def get_person_details(person_id: str):
    response = {
        "data": {
            "id": person_id,
            "name": f"Person {person_id}",
            "email": f"",
            "decks": []
        }
    }
    return response

@router.put("/{person_id}")
async def put_person(person_id: str, person: Person):
    response = {
        "data": {
            "id": person_id,
            "name": person.name,
            "email": person.email
        }
    }
    return response