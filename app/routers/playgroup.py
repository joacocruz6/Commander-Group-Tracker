from fastapi import APIRouter, HttpException


router = APIRouter(prefix='/playgroups', tags=['playgroups'])

@router.post("/")
async def create_new_playgroup():
    response = {
        "data": "Hello World!"
    }
    return response

@router.get("/{playgroup_id}")
async def get_playgroup_details(playgroup_id: str):
    response = {
        "data": {
            "id": playgroup_id
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
    raise HttpException(status_code=404)

@router.put("/{playgroup_id}")
async def update_playgroup(playgroup_id: str):
    response = {
        "data": {
            "id": playgroup_id,
        }
    }
    return response

