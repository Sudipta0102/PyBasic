import json
from json import JSONEncoder


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("ami", 290)


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, "class": o.__class__.__name__}

        return JSONEncoder.default(self, o)


with open("user1.json", 'w') as op_file:
    json.dump(user, op_file, cls=UserEncoder)

