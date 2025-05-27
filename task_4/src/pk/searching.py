from pk.file_operations import FileOperations
import logging


def word_occurance(input: str, words: str) -> dict:
    line_list = FileOperations.read_file(input)
    if line_list is None or words is None:
        logging.error('There is no data to proceed')
        return {}
    count = 0
    words_in = {}
    word_list = [word.lower() for word in words.split(',')]
    logging.info(f'Words to find: {words}')
    for line in line_list:
        for word in word_list:
            for item in line:
                if item.lower() == word:
                    if word not in words_in:
                        count = 1
                    count += 1
                    words_in[word] = count
    return words_in

