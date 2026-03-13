
import json
from aiokafka import AIOKafkaConsumer

from src.logger import logger

from src.models.user_models import CreateUser
from src.database.user_dbmanager import create_user

from src.conf.urls import BROKER_URL


async def consume():
    consumer = AIOKafkaConsumer(
        'user-registration',
        bootstrap_servers=BROKER_URL,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        group_id="item-service"
    )

    # Запускаем консьюмера
    await consumer.start()
    try:
        async for msg in consumer:
            logger.info(f"Получен пользователь: {msg.value}")
            try:
                registration_user = CreateUser(**msg.value)
                if registration_user.type == "student":
                    uuid = registration_user.uuid
                    await create_user(uuid=uuid)
            except Exception as e:
                logger.error(f"Ошибка обработки сообщения: {e}")
    finally:
        await consumer.stop()