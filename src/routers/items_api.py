from typing import List

from fastapi import APIRouter, Request, Depends, Cookie, Query
from src.database import inventory_dbmanager, item_dbmanager
from lib.fast_token import authorize_user, get_uuid_of_token

router = APIRouter()


@router.get("/get-items-of-user", dependencies=[Depends(authorize_user)])
async def get_items_of_my_user(request: Request, item_id: int = None, jwt: str = Cookie(None)):
    uuid = get_uuid_of_token(jwt)
    return await inventory_dbmanager.get_items_of_user(user_uuid=uuid)


@router.get("/get-items-of-user/{user_uuid}", dependencies=[Depends(authorize_user)])
async def get_items_of_user(request: Request, user_uuid: str, inventory_id: int = None):
    return await inventory_dbmanager.get_items_of_user(user_uuid=user_uuid)


@router.get("/get-item")
async def get_item(request: Request, item_id: int):
    if not item_id:
        return
    return (await item_dbmanager.get_items([item_id]))[0]

@router.get("/get-item-list")
async def get_item_list(request: Request, item_ids: List[int] = Query(...)):
    if not item_ids:
        return
    print(item_ids, await item_dbmanager.get_items(item_ids))
    return await item_dbmanager.get_items(item_ids)
