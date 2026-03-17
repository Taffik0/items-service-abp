from uuid import UUID
from src.database.repository.item_repository import ItemRepository
from src.database.unit_of_work import UoW

from src.models.item_models import Item, UserItem
from src.models.mappers.items_mapper import item_dbdto_to_dto, user_item_dbdto_to_dto


class ItemService:
    def __init__(self, uow: UoW, item_repo: ItemRepository):
        self.item_repo = item_repo
        self.uow = uow

    async def get_item(self, item_id: int) -> Item | None:
        item_db = await self.get_item(item_id)
        if item_db is None:
            return None
        return item_dbdto_to_dto(item_db)

    async def get_item_by_ids(self, ids: list[int]) -> list[Item]:
        items_db = await self.item_repo.get_items_by_ids(ids)
        return [item_dbdto_to_dto(item_db) for item_db in items_db]

    async def get_items_of_user(self, user_uuid: UUID) -> list[UserItem]:
        user_items_db = await self.get_items_of_user(user_uuid)
        return [user_item_dbdto_to_dto(user_item_db) for user_item_db in user_items_db]
