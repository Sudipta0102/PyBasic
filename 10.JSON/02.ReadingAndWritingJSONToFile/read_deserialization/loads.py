# 1. The advantage with loads is, instead of taking filepath (which load() demands) it can take JSON string,
# and the parsing will happen.
# 2. Also, If file content is a Json string. You can do the following:
#   a. you can open the file in a read mode.
#   b. And with that fileobject you can do fileobject.read()
#   c. this fileobject.read() will be the argument of loads()


# 1. Read json file from a string

# JSON string
import json

a = '{"name": "Bob", "languages": "English"}'

# can pass this directly to the loads() method.
data1 = json.loads(a)

print(data1)


# 2. Reading from file using loads()
f = open('sampleRead.json', 'r')

data2 = json.loads(f.read())

print(data2['data'])

