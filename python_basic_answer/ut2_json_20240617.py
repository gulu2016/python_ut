import json



def extract_user_info(json_string):
    data = json.loads(json_string)
    user = data.get('user', {})
    user_name = user.get('name', 'Unknown Name')
    user_age = user.get('age', 'Unknown Age')
    user_city = user.get('address', {}).get('city', 'Unknown City')
    return f"User's name is {user_name}, age is {user_age}, and lives in {user_city}."

if __name__ == '__main__':
    json_string1 = '{"user": {"age": 28, "address": {"street": "1234 Elm Street", "city": "Springfield", "zipcode": "62704"}}}'
    json_string2 = '{"user": {}}'

    print(extract_user_info(json_string1))
    print(extract_user_info(json_string2))