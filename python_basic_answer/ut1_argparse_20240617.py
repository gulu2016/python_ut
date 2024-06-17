import argparse


def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for line in f)


def process_file(filename, to_uppercase=False, to_lowercase=False):
    content = ''
    with open(filename, 'r') as f:
        content = f.read()
        if to_uppercase:
            content = content.upper()
        elif to_lowercase:
            content = content.lower()
    return content


def main():
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('filenames', metavar='F', type=str, nargs='+', help='files to be processed')
    parser.add_argument('-c', '--count', action='store_true', help='count the number of lines in each file')
    parser.add_argument('-u', '--uppercase', action='store_true', help='convert file content to uppercase')
    parser.add_argument('-l', '--lowercase', action='store_true', help='convert file content to lowercase')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')

    args = parser.parse_args()

    for file in args.filenames:
        if args.verbose:
            print(f"Processing file: {file}")

        if args.count:
            print(f"count of lines: {count_lines(file)}")

        if args.uppercase or args.lowercase:
            print(f"content of file is {process_file(file,args.uppercase,args.lowercase)}")

if __name__ == '__main__':
    main()