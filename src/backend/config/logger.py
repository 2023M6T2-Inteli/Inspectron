import logging
import sys


class Console:
    @staticmethod
    def log(info):
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
        logger = logging.getLogger(__name__)

        logger.info(info)
