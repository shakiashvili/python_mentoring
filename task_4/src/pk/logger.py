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
if __name__ == '__main__':
    logger_config()
