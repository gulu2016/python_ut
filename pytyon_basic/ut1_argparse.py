# description: argparse module quick start
# date: 2024-06-16

'''
练习题目
编写一个 Python 脚本，用于处理一组文件并执行不同的操作。具体要求如下：

脚本接受一个或多个文件名作为位置参数。
脚本支持以下可选参数：
-c 或 --count：统计每个文件中的行数。
-u 或 --uppercase：将每个文件的内容转换为大写并输出。
-l 或 --lowercase：将每个文件的内容转换为小写并输出。
-v 或 --verbose：输出详细信息，包括处理的文件名和操作类型。
'''

'''
假设你的脚本名为 file_processor.py，可以按照以下方式使用：

输入：
python file_processor.py file1.txt file2.txt -c -v

输出：
Processing file: file1.txt
Lines count: 100

Processing file: file2.txt
Lines count: 150


输入：
python file_processor.py file1.txt file2.txt -u

输出：
CONTENT OF FILE1.TXT IN UPPERCASE
CONTENT OF FILE2.TXT IN UPPERCASE
'''


import argparse


def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)


def process_file(filename, to_uppercase=False, to_lowercase=False):
    with open(filename, 'r') as file:
        content = file.read()
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

    for filename in args.filenames:
        if args.verbose:
            print(f'Processing file: {filename}')

        if args.count:
            line_count = count_lines(filename)
            print(f'Lines count: {line_count}')

        if args.uppercase or args.lowercase:
            content = process_file(filename, to_uppercase=args.uppercase, to_lowercase=args.lowercase)
            print(content)


if __name__ == '__main__':
    main()


