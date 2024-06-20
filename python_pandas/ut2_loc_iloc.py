import pandas as pd

# 创建示例 DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
        'age': [24, 27, 22, 32, 29],
        'score': [88, 92, 95, 70, 85]}

df = pd.DataFrame(data)

# ut2-1: loc接收数字，使用标签选择单行
print(df.loc[1])  # 选择索引为 1 的行

# ut2-2: loc接收切片和数组， 使用标签选择多行多列
print(df.loc[0:2, ['name', 'age']])  # 选择索引 0 到 2 的行和 'name'、'age' 列

# ut2-3: loc接收bool表达式，  使用布尔索引选择行
print(df.loc[df['age'] > 25])

# ut2-4: 使用整数位置选择单行
print(df.iloc[1])  # 选择第二行（索引位置为 1）

# ut2-5: 使用整数位置选择多行多列
print(df.iloc[0:2, 0:2])  # 选择前两行和前两列

# ut2-6:  使用布尔索引选择行（需要将布尔索引转换为整数位置）
print(df.iloc[(df['age'] > 25).values])
