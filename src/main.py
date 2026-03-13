import asyncio

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from contextlib import asynccontextmanager

from src.logger import logger

from src.database import dbmanager

from src.routers import routers_init

from src.kafka import kafka_init

@asynccontextmanager
async def lifespan(app: FastAPI):
    await dbmanager.load()
    await kafka_init.init()
    logger.info("started")
    yield
    logger.info("stop")
    await dbmanager.close()

    await kafka_init.stop()

app = FastAPI(lifespan=lifespan)

app.include_router(routers_init.routers)

app.mount("/media", StaticFiles(directory="media"), name="media")


if __name__ == "__main__":
    uvicorn.run("src.main:app", port=5020, reload=True)