import asyncio

from .kafaka_listaner import KafkaListener

from .handlers.reg_handler import UserRegistrationHandler
from .handlers.collection_reward_handler import CollectionRewardHandler

from src.conf.urls import BROKER_URL


GROUP_ID = "item-service"
BOOTSTRAP_SERVICE = BROKER_URL

KAFKA_LISTENERS: list[KafkaListener] = [KafkaListener(GROUP_ID,
                         [UserRegistrationHandler(), CollectionRewardHandler()],
                                        BOOTSTRAP_SERVICE)]

kafka_tasks = []


async def init():
    for kafka_listener in KAFKA_LISTENERS:
        kafka_task = asyncio.create_task(kafka_listener.consume())
        kafka_tasks.append(kafka_task)


async def stop():
    for kafka_task in kafka_tasks:
        kafka_task.cancel()
        try:
            await kafka_task
        except asyncio.CancelledError:
            pass