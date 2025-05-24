from pk.decorator import decorator_function
from pk.cli import argument_parsing
from pk.file_operations import FileOperations
from pk.searching import search
from pk.logger import log_error


@decorator_function
def main() -> dict:
    try:
        input_file, words, output_file = argument_parsing()
        search_result = search(input_file, words)
        FileOperations.write_file(output_file, search_result)
        return search_result
    except Exception as e:
        log_error(f'An error occured: {e}')
        raise


if __name__ == '__main__':
    main()