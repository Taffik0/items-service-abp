import asyncpg
from contextlib import asynccontextmanager
from src.conf.db_conf import USER, DB_URL, PASSWORD, DATABASE

db_pool: asyncpg.Pool = None


async def load():
    global db_pool
    db_pool = await asyncpg.create_pool(
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        host=DB_URL,
        port=5432,
        min_size=1,
        max_size=10,
    )
    print(db_pool)

async def close():
    await db_pool.close()