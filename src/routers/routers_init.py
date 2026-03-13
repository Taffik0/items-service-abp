from fastapi import APIRouter

from src.routers import items_api, internal_router

routers = APIRouter()

routers.include_router(items_api.router)
routers.include_router(internal_router.router)
