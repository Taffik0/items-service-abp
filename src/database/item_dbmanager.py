from src.database import dbmanager
from src.logger import logger


async def get_items(item_ids):
    async with dbmanager.db_pool.acquire() as conn:
        rows = await conn.fetch("""SELECT * FROM items WHERE item_id = ANY($1)""", item_ids)
        # Создаём словарь для быстрого поиска
        rows_map = {row['item_id']: row for row in rows}
        # Возвращаем в том же порядке, что и item_ids
        return [rows_map[i] for i in item_ids]



