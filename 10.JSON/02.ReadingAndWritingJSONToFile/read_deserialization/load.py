import json
import demjson

# json.load() takes a file object and returns python object.
with open('sampledump.json', 'r') as input_file:
    json_obj = json.load(input_file)

print(json_obj)

# 1. Desirialization of JSON:
# it means the conversion of JSON objects to their python objects.
#
# 2. How do we do this in python?
# load()/loads() method is used for that. It belongs to json module.
#
# 3. process->
# if you have json in a .json file or or string format of json, then
# with the help of load()/ loads() I can easily deserialize.
#
# Things to remember:
# 1. From json object It generates a dictionary
# 2. From json Array it generates a List

