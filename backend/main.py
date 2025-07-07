import os

from logging_config import setup_logging
import logging

if __name__ == "__main__":
    # TODO: make shit work.

    setup_logging()

    logger = logging.getLogger('numifocus.main')
    logger.info("Starting NumiFocus")

    pass
        
    print(os.environ.get("INSTRUMENT_DATA"))
