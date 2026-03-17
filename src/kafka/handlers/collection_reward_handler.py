from aiokafka import ConsumerRecord

from database.unit_of_work import UoW

from .message_handler import MessageHandler

from src.logger import logger

from src.models.item_model import CollectionReward

from src.database.inventory_dbmanager import add_item_to_user

from src.services.processed_broker_message import ProcessedBrokerMessageService
from src.models.broker_events.broker_event_types import BrokerEventType


class CollectionRewardHandler(MessageHandler):
    _topic = "collection_reward"

    async def process_message(self, msg: ConsumerRecord):
        reward = CollectionReward(**msg.value)
        logger.info(
            f"collected by {reward.user_uuid} ({reward.type} {reward.id})")
        if reward.type == "item":
            logger.info(f"получилось")
            await add_item_to_user(reward.user_uuid, reward.id)


class CollectionRewardHandlerId(MessageHandler):
    _topic = "collection_reward"

    def __init__(self, process_message_service: ProcessedBrokerMessageService, uow: UoW):
        self.process_message_service = process_message_service
        self.uow = uow

    async def process_message(self, msg: ConsumerRecord):
        reward = CollectionReward(**msg.value)
        marker_exist = await self.process_message_service.exists_marker(
            event_id=reward.event_id, event_type=BrokerEventType.COLLECTED_REWARD)
        if marker_exist:
            return
        self.process_message_service.mark_as_processed(
            event_id=reward.event_id, event_type=BrokerEventType.COLLECTED_REWARD)
        logger.info(
            f"collected by {reward.user_uuid} ({reward.type} {reward.id})")
        if reward.type == "item":
            logger.info(f"получилось")
            await add_item_to_user(reward.user_uuid, reward.id)
