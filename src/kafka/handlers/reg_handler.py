from aiokafka import ConsumerRecord
from .message_handler import MessageHandler
from src.logger import logger

from src.models.user_models import CreateUser
from src.database.user_dbmanager import create_user


class UserRegistrationHandler(MessageHandler):
    _topic = "user-registration"

    async def process_message(self, msg: ConsumerRecord):
        logger.info(f"Получен пользователь: {msg.value}")
        try:
            registration_user = CreateUser(**msg.value)
            if registration_user.type == "student":
                uuid = registration_user.uuid
                await create_user(uuid=uuid)
        except Exception as e:
            logger.error(f"Ошибка обработки сообщения: {e}")
