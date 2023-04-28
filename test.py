def nested_dict(input_dict, string):
    key_list = string.split('.')
    for item in key_list:
        input_dict = input_dict.get(item)
    return input_dict

# e.g
# input_dict = {'foo': {'bar': 2}, 'hello': 5, 'richa': {'age': 25, 'height': '5ft'}}
# string = 'foo.bar'
# should return 2

print(nested_dict({'foo': {'bar': 2}, 'hello': 5, 'richa': {'age': 25, 'height': '5ft'}}, 'foo.bar'))