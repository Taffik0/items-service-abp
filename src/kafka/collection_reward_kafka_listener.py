import json
from aiokafka import AIOKafkaConsumer
from src.logger import logger

from src.models.item_model import CollectionReward

from src.database.inventory_dbmanager import add_item_to_user

from src.conf.urls import BROKER_URL


async def consume():
    logger.info("start collection_reward")
    consumer = AIOKafkaConsumer(
        'collection_reward',
        bootstrap_servers=BROKER_URL,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id="item-service"
    )

    # Запускаем консьюмера
    await consumer.start()
    try:
        async for msg in consumer:
            reward = CollectionReward(**msg.value)
            logger.info(f"collected by {reward.user_uuid} ({reward.type} {reward.id})")
            if reward.type == "item":
                logger.info(f"получилось")
                await add_item_to_user(reward.user_uuid, reward.id)
    finally:
        await consumer.stop()
