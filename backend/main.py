import os

from fastapi import FastAPI
import logging
from .routes import router

from logging_config import setup_logging

if __name__ == "__main__":
    # TODO: make shit work.

    setup_logging()

    logger = logging.getLogger('numifocus.main')
    logger.info("Starting NumiFocus")

    app = FastAPI()
    app.include_router(router)

    @app.get("/")
    def root():
        return {"message": "Hello from FastAPI!"}
        