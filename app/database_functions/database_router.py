from fastapi import APIRouter

from ..database import Database


router = APIRouter()


@router.get("/{db_name}/exists")
async def db_exists(db_name: str):
    db = Database.get_database(db_name)
    ping = await db.command("ping")
    return {"exists": ping["ok"]}

# @router.get("/{db_name}/obj_team")
# async def get_obj_tim(db_name: str):
#     db = Database.get_database(db_name)
#     data = await db["obj_team"].find({}, {"_id": 0}).to_list(length=None)
#     return data

@router.get("/{db_name}/{collection_name}")
async def get_collection(db_name: str, collection_name: str):
    db = Database.get_database(db_name)
    data = await db[collection_name].find({}, {"_id": 0}).to_list(length=None)
    return data