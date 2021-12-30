import json

# opening json file
f = open('sampleRead.json')

# Return json object as python dictionary
# load takes a 'filepath' arg as a mandatory argument.
data = json.load(f)

print(type(data))

print(data['data'])


f.close()
