import logging


def main() -> None:
    logging.basicConfig(level=logging.INFO, filename="l.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.info('Sgaha')
    logging.error('OOps this is error fix it')
    logging.warning('This is warning')


if __name__ == '__main__':
    main()
