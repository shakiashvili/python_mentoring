from pk.decorator import decorator_function_to_calculate_execution_time as deco
from pk.cli import argument_parsing
from pk.file_operations import FileOperations
from pk.searching import word_occurance
import logging


@deco
def main() -> dict:
    try:
        input_file, words, output_file = argument_parsing()
        search_result = word_occurance(input_file, words)
        FileOperations.write_file(output_file, search_result)
        return search_result
    except Exception as e:
        logging.error(f'An error occured: {e}')


main()