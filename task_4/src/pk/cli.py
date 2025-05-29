import argparse
import logging


def argument_parsing() -> None:
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
        return logging.error(f'We are having an problem: {e}')
        