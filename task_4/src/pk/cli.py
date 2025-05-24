import argparse
from pk.logger import log_error


def argument_parsing() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to input file',
                        required=True)
    parser.add_argument('-w', '--words', help='Words to be found', 
                        required=True)
    parser.add_argument('-o', '--output', help='This is output file', 
                        required=True)
    try:
        args = parser.parse_args()
        input_file = args.input
        words = args.words
        output_file = args.output 
        return input_file, words, output_file
    except Exception as e:
        return log_error(f'We are having an problem: {e}')


if __name__ == '__main__':
    input_file, words, output_file = argument_parsing()