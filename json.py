import json
# print(dir(json))
# print(help(json.__loader__))
string = 'Hi, my name in Ben'
json_string = json.dumps(string)
print(json_string)
