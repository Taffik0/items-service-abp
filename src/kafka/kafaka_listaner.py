import json

from aiokafka import AIOKafkaConsumer
from aiokafka.structs import ConsumerRecord

from .handlers.message_handler import MessageHandler
from ..logger import logger


class KafkaListener:
    def __init__(self, group_id: str, message_handlers: list[MessageHandler], bootstrap_servers: str):
        self.group_id = group_id
        self.message_handlers: dict[str, MessageHandler] = {msg_handler.get_topic(): msg_handler
                                                            for msg_handler in message_handlers}
        self.topics = [msg_handler.get_topic() for msg_handler in message_handlers]
        self.bootstrap_servers = bootstrap_servers

    async def consume(self):
        logger.info("kafka_listener - started")
        consumer = AIOKafkaConsumer(
            *self.topics,
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            group_id=self.group_id
        )

        # Запускаем консьюмера
        await consumer.start()
        try:
            async for msg in consumer:
                handler = self.message_handlers.get(msg.topic)
                if not handler:
                    logger.warning(f"No handler for topic {msg.topic}")
                    continue

                try:
                    await handler.process_message(msg)
                    await consumer.commit()
                except Exception as e:
                    logger.exception("Message processing failed")

        finally:
            await consumer.stop()