'''
问题描述
你有一个包含用户信息的 JSON 字符串，你需要将其解析为 Python 字典并从中提取特定信息。请按以下步骤完成任务：

将给定的 JSON 字符串解析为 Python 字典。
提取用户的姓名（name）、年龄（age）和地址中的城市（city）。
如果地址中的城市不存在，返回 "Unknown City"。
将提取的信息格式化为一个字符串，格式如下：
"User's name is [name], age is [age], and lives in [city]."

给定的 JSON 字符串
{
    "user": {
        "name": "John Doe",
        "age": 28,
        "address": {
            "street": "1234 Elm Street",
            "city": "Springfield",
            "zipcode": "62704"
        }
    }
}


要求
编写一个函数 extract_user_info，接受一个 JSON 字符串作为参数，并返回格式化的字符串。如果 JSON 字符串中缺少某些键，应处理这些情况以避免抛出错误。

示例
输入：
json_string = '{"user": {"name": "John Doe", "age": 28, "address": {"street": "1234 Elm Street", "city": "Springfield", "zipcode": "62704"}}}'
输出：
"User's name is John Doe, age is 28, and lives in Springfield."

'''

import json


def extract_user_info(json_string):
    # 步骤1：将 JSON 字符串解析为 Python 字典
    data = json.loads(json_string)

    # 步骤2：提取用户信息
    name = data.get('user', {}).get('name', 'Unknown')
    age = data.get('user', {}).get('age', 'Unknown')
    city = data.get('user', {}).get('address', {}).get('city', 'Unknown City')

    # 步骤4：格式化字符串
    result = f"User's name is {name}, age is {age}, and lives in {city}."

    return result


# 测试
json_string = '{"user": {"name": "John Doe", "age": 28, "address": {"street": "1234 Elm Street", "city": "Springfield", "zipcode": "62704"}}}'
print(extract_user_info(json_string))
