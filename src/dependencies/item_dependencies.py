from fastapi import Depends

from database.unit_of_work import UoW
from src.database.dbmanager import get_conn

from src.database.repository.item_repository import ItemRepository, ItemRepositoryPg
from src.services.item_service import ItemService


def get_uow(conn=Depends(get_conn)) -> UoW:
    return UoW(conn=conn)


def get_item_repository(conn=Depends(get_conn)) -> ItemRepository:
    return ItemRepositoryPg(conn=conn)


def get_item_service(
        item_repo=Depends(get_item_repository),
        uow=Depends(get_uow)) -> ItemService:
    return ItemService(uow=uow, item_repo=item_repo)
