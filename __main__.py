import uvicorn

from src.configs import settings
from src.loggers import get_logger

logger = get_logger(name="debug_logger", level=settings.app.log_level)


def start_application():
    uvicorn.run("src.core:extractor_app.fastapi_app",
                host=settings.app.host,
                port=settings.app.port,
                reload=settings.app.debug)



if __name__ == "__main__":
    logger.info("[#] Starting service...")
    logger.info(f"[#] DEBUG={settings.app.debug}")
    try:
        start_application()
    except KeyboardInterrupt:
        logger.info("[#] Stopping service...")
    except RuntimeError as e:
        logger.info(f"[X] Error: {e}")
