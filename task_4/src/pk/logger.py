import logging


def logger_config():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("tool.log"),
            logging.StreamHandler()
            ]
        )

