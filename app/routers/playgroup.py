from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4, UUID

router = APIRouter(prefix='/playgroups', tags=['playgroups'])

class Playgroup(BaseModel):
    name: str = Field(max_length=64)

@router.post("/")
async def create_new_playgroup(playgroup: Playgroup):
    uuid = str(uuid4())
    response = {
        "data": {
            "id": uuid,
            "name": playgroup.name
        }
    }
    return response

@router.get("/admin")
async def get_user_created_playgroups():
    response = {
        "playgroups": [
            {
                "playgroup_id": "1"
            },
            {
                "playgroup_id": "2"
            }
        ]
    }
    return response

@router.get("/participant")
async def get_user_playgroup_participant():
    raise HTTPException(status_code=404)

@router.get("/{playgroup_id}")
async def get_playgroup_details(playgroup_id: UUID):
    response = {
        "data": {
            "id": str(playgroup_id),
            "name": f"Playgroup {playgroup_id}"
        }
    }
    return response

@router.put("/{playgroup_id}")
async def update_playgroup(playgroup_id: UUID, playgroup: Playgroup):
    response = {
        "data": {
            "id": str(playgroup_id),
            "name": playgroup.name
        }
    }
    return response

@router.delete("/{playgroup_id}")
async def delete_playgroup(playgroup_id: UUID):
    response = {
        "data": {
            "id": str(playgroup_id),
            "message": f"Playgroup {playgroup_id} deleted successfully"
        }
    }
    return response
