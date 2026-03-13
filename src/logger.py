import logging
import os

from src.path import LOGS_DIR

# Убедись, что папка logs существует
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

# Общий формат логов
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Файл
file_handler = logging.FileHandler(LOGS_DIR / "app.log", encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # логировать всё
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
