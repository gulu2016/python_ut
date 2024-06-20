# description: 总结各种筛选pandas dataframe的方法
import pandas as pd

# 创建示例 DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
        'age': [24, 27, 22, 32, 29],
        'score': [88, 92, 95, 70, 85]}

df = pd.DataFrame(data)


# ut1-1: 使用 bool表达式，筛选年龄大于25的行
filtered_df = df[df['age'] > 25]
print(filtered_df)


# ut1-2: 使用 query，筛选年龄大于25的行
filtered_df = df.query('age > 25')
print(filtered_df)

# ut1-3: 使用 loc，loc可以接收bool表达式和数字， 筛选年龄大于25的行
filtered_df = df.loc[df['age'] > 25]
print(filtered_df)

# ut1-4: 使用iloc，iloc只能接收数字，筛选年龄大于25的行
filtered_df = df.iloc[(df['age'] > 25).values]
print(filtered_df)


# ut1-5: 使用多个表达式，连接查询条件， 筛选年龄大于25且成绩大于80的行
filtered_df = df[(df['age'] > 25) & (df['score'] > 80)]
print(filtered_df)


# 筛选年龄大于25且成绩大于80的行
filtered_df = df.query('age > 25 and score > 80')
print(filtered_df)


# # ut1-6： 使用 apply方法和bool表达式，筛选名字长度大于3的行
filtered_df = df[df['name'].apply(len) > 3]
print(filtered_df)

