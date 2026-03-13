from src.database import dbmanager


async def create_user(uuid):
    async with dbmanager.db_pool.acquire() as conn:
        record = await conn.fetch("""INSERT INTO users (user_uuid) VALUES ($1)""", uuid)