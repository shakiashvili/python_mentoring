import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("tool.log"),
        logging.StreamHandler()
    ]
)


def log_info(message: str) -> str:
    logging.info(message)


def log_error(message: str) -> str:
    logging.error(message)


def log_warning(message: str) -> str:
    logging.warning(message)
