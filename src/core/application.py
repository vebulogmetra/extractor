from fastapi import FastAPI

from src.api.routers.root import router as root_router
from src.configs import settings


class Exctractor:
    def __init__(self):
        self.fastapi_app = None
        self._setup()
        self._build_fastapi()

    def _build_fastapi(self):
        self.fastapi_app = FastAPI(
            title="Exctractor application API",
            version=settings.app.version,
            docs_url=settings.app.docs_url,
            redoc_url=None,
        )

        self.fastapi_app.include_router(router=root_router)

    def _setup(self): ...

    def shutdown(self): ...
