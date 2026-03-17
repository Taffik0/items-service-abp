from typing import List
from uuid import UUID

from fastapi import APIRouter, Request, Depends, Cookie, Query
from src.database import inventory_dbmanager, item_dbmanager
from lib.fast_token import authorize_user, get_uuid_of_token, AuthToken, require_auth
from pydantic import BaseModel


router = APIRouter()


class ItemsBatchIn(BaseModel):
    ids: list[int]


@router.get("/get-items-of-user", dependencies=[Depends(authorize_user)])
async def get_items_of_my_user_legacy(request: Request, item_id: int = None, jwt: str = Cookie(None)):
    uuid = get_uuid_of_token(jwt)
    return await inventory_dbmanager.get_items_of_user(user_uuid=uuid)


@router.get("/get-items-of-user/{user_uuid}", dependencies=[Depends(authorize_user)])
async def get_items_of_user_legacy(request: Request, user_uuid: str, inventory_id: int = None):
    return await inventory_dbmanager.get_items_of_user(user_uuid=user_uuid)


@router.get("/get-item")
async def get_item_legacy(request: Request, item_id: int):
    if not item_id:
        return
    return (await item_dbmanager.get_items([item_id]))[0]


@router.get("/get-item-list")
async def get_item_list_legacy(request: Request, item_ids: List[int] = Query(...)):
    if not item_ids:
        return
    print(item_ids, await item_dbmanager.get_items(item_ids))
    return await item_dbmanager.get_items(item_ids)


@router.get("/users/my/items")
async def get_items_of_my_user(
    token: AuthToken = Depends(require_auth)
):
    pass


@router.get("/items/{item_id}")
async def get_item(
    item_id: int,
    token: AuthToken = Depends(require_auth)
):
    pass


@router.get("/users/{user_uuid}/items")
async def get_items_of_user(
    user_uuid: UUID,
    token: AuthToken = Depends(require_auth)
):
    pass


@router.post("/items/bulk")
async def get_batch_items(
    items_batch_in: ItemsBatchIn,
    token: AuthToken = Depends(require_auth)
):
    pass
