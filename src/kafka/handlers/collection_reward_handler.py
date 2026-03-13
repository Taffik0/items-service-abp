from aiokafka import ConsumerRecord

from .message_handler import MessageHandler

from src.logger import logger

from src.models.item_model import CollectionReward

from src.database.inventory_dbmanager import add_item_to_user


class CollectionRewardHandler(MessageHandler):
    _topic = "collection_reward"

    async def process_message(self, msg: ConsumerRecord):
        reward = CollectionReward(**msg.value)
        logger.info(f"collected by {reward.user_uuid} ({reward.type} {reward.id})")
        if reward.type == "item":
            logger.info(f"получилось")
            await add_item_to_user(reward.user_uuid, reward.id)
