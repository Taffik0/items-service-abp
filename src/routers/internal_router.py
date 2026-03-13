from fastapi import APIRouter, Request

import httpx

from src.database.internal_db import write_last_users_row

router = APIRouter()

@router.get("/synch-users")
async def synch_users(request: Request, count: int = 1):
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"http://127.0.0.1:5000/last-row?count={count}"
        )
        data = resp.json()
        await write_last_users_row(data)
