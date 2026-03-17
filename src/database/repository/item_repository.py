from dataclasses import dataclass
from uuid import UUID
from asyncpg import Connection
from src.models.item_models import ItemDBDTO


class ItemRepository:
    async def get_item(id: int) -> ItemDBDTO | None:
        pass

    async def get_items_by_ids(ids: list[int]) -> list[ItemDBDTO]:
        pass

    async def get_items_of_user(self, user_uuid: UUID) -> list[ItemDBDTO]:
        pass

    async def give_item_to_user(self, item_id: int, user_uuid: UUID) -> bool:
        pass

    async def create_item():
        pass


class ItemRepositoryPg(ItemRepository):
    def __init__(self, conn: Connection):
        self.conn = conn

    def _item_to_db_dto(self, record) -> ItemDBDTO:
        return ItemDBDTO(
            id=record["item_id"],
            name=record["name"],
            type=record["type"],
            icon_path=record["icon_path"],
            description=record["description"])

    async def get_item(self, id: int) -> ItemDBDTO | None:
        query = """SELECT item_id, name, description, icon_path, type FROM items WHERE item_id = $1"""
        record = await self.conn.fetchrow(query, id)
        if record is None:
            return None
        return self._item_to_db_dto(record)

    async def get_items_by_ids(self, ids: list[int]) -> list[ItemDBDTO]:
        query = """SELECT item_id, name, description, icon_path, type FROM items WHERE item_id = ANY($1::int[])"""
        records = self.conn.fetch(query, ids)
        return [self._item_to_db_dto(record) for record in records]

    async def get_items_of_user(self, user_uuid: UUID) -> list[ItemDBDTO]:
        query = """
        SELECT
            it.item_id, it.name, it.description, it.icon_path, it.type FROM inventories AS in
        JOIN items AS it ON it.item_id =  in.item_id
        WHERE user_uuid = $1"""
        records = await self.conn.fetch(query, ids)
        return [self._item_to_db_dto(record) for record in records]

    async def give_item_to_user(self, item_id: int, user_uuid: UUID) -> bool:
        query = """
        INSERT INTO inventories (user_uuid, item_id) VALUES ($1, $2)"""
        result = await self.conn.execute(query, user_uuid, item_id)
        return result.split()[2] == "1"
