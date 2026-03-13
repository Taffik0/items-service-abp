from src.database import dbmanager


async def write_last_users_row(users):
    query = """
        INSERT INTO users (user_uuid, type)
        VALUES ($1, $2)
        ON CONFLICT (user_uuid) DO NOTHING
    """
    async with dbmanager.db_pool.acquire() as conn:
        async with conn.transaction():
            await conn.executemany(
                query,
                [(user["id"], user["type"]) for user in users]
            )
