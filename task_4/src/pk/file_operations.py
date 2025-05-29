import logging
import os


class FileOperations:
    @staticmethod
    def read_file(file_path: str) -> list:
        try:
            with open(file_path) as input_file:
                current = os.path.abspath(__file__)
                logging.info(current)
                logging.info(f'Reading the input file, {file_path}')
                return [line.strip().split() for line in input_file.readlines()]
        except FileNotFoundError:
            logging.error("File not Found,Please use the correct path")
        except Exception as e:
            logging.error(f"We have an error: {e}")

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        try:
            with open(file_path, 'w') as output_file:
                logging.info(f'Writing into, {file_path}')
                output_file.write(str(content) + '\n')
        except Exception as e:
            logging.error(f"We have an error: {e}")
            