import argparse
from decor import decorator_func
from exceptions import EmptyFileError


@decorator_func
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    text = ''
    lst = []
    try: 
        with open(input_file, 'r') as inf:
            with open(output_file, 'w') as ouf:
                first_char = inf.read(1)
                if not first_char:
                    raise EmptyFileError("File is empty")
                for text in inf.readlines():
                    words = text.split()
                    for i in words:
                        if i.lower() == 'epam' or i.lower() == 'giorgi':
                            lst.append(i)
                ouf.write(' '.join(lst))
    except FileNotFoundError:
        print("File not Found,Please use the correct path")
    except Exception as e:
        print(f'We are having an error: {e}')


if __name__ == "__main__":
    main()
# To run this python3 command_line.py -i sometext.txt -o text.txt