from pk.file_operations import FileOperations
from pk.logger import log_error, log_info


def search(input: str, words: str) -> dict:
    line_list = FileOperations.read_file(input)
    if line_list is None or words is None:
        log_error('There is no data to proceed')
        return {}
    count = 0
    words_in = {}
    word_list = [word.lower() for word in words.split(',')]
    log_info(f'Words to find: {words}')
    for line in line_list:
        for word in word_list:
            for item in line:
                if item.lower() == word:
                    count += 1
                    words_in[word] = count
    return words_in

