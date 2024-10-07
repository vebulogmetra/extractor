from fastapi import Request
from fastapi.responses import JSONResponse
from time import monotonic

from fastapi import APIRouter, status

from src.loggers import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.get("/health_check")
def health_check_handler(request: Request):
    """Check if the server is up and running."""
    logger.info("Health check request received")
    start_time = monotonic()
    # Simulate some processing time
    for _ in range(1000000):
        pass
    end_time = monotonic()
    logger.info(f"Health check took {end_time - start_time:.6f} seconds")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Server is healthy"})
