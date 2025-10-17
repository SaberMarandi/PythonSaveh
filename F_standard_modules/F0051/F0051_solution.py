# F0051 - کار با JSON
# تبدیل دیکشنری به JSON

import json

name = input()
age = int(input())

data = {
    "name": name,
    "age": age
}

json_string = json.dumps(data)
print(json_string)
