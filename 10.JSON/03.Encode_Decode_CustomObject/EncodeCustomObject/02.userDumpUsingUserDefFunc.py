# 1. in the first file, we came across a type error for which we need to convert the object
# into a dictionary
# 2. This is the first way to conver an object to dictionary

import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("ami", 290)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, 'Class': o.__class__.__name__}
    else:
        raise TypeError('Object of type TextIOWrapper is not JSON serializable')


with open('user.json', 'w') as op_file:
    json.dump(user, op_file, default=encode_user, indent=2)




