# 1. any serialization would take a dictionary and convert it json string or can write to a file
# as per user's choice,
# 2. but let's say, there is a situation where you have custom object and you want a
# JSON out of it.
# 3. what you can't do is below operation where you can't convert to a JSON file or string from
# the object itself. you will need to encode it first to make it a dictionary.

import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("ami", 290)
with open("user.json", 'w') as op_file:
    json.dump(op_file, user)
