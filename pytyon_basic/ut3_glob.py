'''
问题描述：

假设你有一个名为 data 的目录，其中包含以下文件：

data/
├── report_2023.txt
├── report_2022.txt
├── summary_2023.txt
├── summary_2022.txt
├── data_2023.csv
├── data_2022.csv
└── archive/
    ├── report_2021.txt
    ├── summary_2021.txt
    └── data_2021.csv

请使用 glob 模块编写一个 Python 脚本，查找并打印 data 目录及其子目录中所有以 report 开头并以 .txt 结尾的文件。

要求：

脚本应能够递归查找 data 目录及其所有子目录中的文件。
输出的文件路径应包含相对路径。
提示：

使用 glob.glob 函数，并设置 recursive=True 参数。
匹配模式可以使用 ** 表示递归子目录。
'''

import glob

# 使用glob查找匹配的文件
files = glob.glob('data/**/report*.txt', recursive=True)

# 打印匹配的文件路径
for file in files:
    print(file)







