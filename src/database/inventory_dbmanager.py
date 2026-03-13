from src.database import dbmanager
from src.logger import logger


async def add_item_to_user(user_uuid:str, item_id: int):
    async with dbmanager.db_pool.acquire() as conn:
        await conn.fetchrow("""INSERT INTO "inventories" (user_uuid, item_id) VALUES ($1, $2)""",
                            user_uuid, item_id)


async def get_items_of_user(user_uuid: str, inventory_id: int = None, limit: int | None = None, offset: int = 0):
    query = f"""
        SELECT
          it.item_id,
          it.type,
          it.name,
          it.description,
          it.icon_path
        FROM inventories ins
        JOIN items it ON ins.item_id = it.item_id
        WHERE ins.user_uuid = $1
    """

    params = [user_uuid]

    if limit is not None:
        query += " LIMIT $2 OFFSET $3"
        params.extend([limit, offset])
    else:
        query += " OFFSET $2"
        params.append(offset)

    async with dbmanager.db_pool.acquire() as conn:
        ret = await conn.fetch(query, *params)
        logger.info(ret)
        return ret