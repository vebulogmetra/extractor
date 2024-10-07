import logging
from pathlib import Path

from src.configs import settings

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
logs_dir = Path(settings.app.logs_dir)


def get_logger(name: str, level: int = settings.app.log_level):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
