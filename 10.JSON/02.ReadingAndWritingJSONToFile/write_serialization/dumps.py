import json

# Data to be written
dictionary ={
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# serializing json
json_obj = json.dumps(dictionary, indent=5)

print(json_obj)

# writing to sample.json
with open("sampledumps.json", 'w') as outputFile:
    outputFile.write(json_obj)


# 1. dumps() function helps in converting a dictionary to json object.
# 2. After conversion, I can write it to a file using write() function.

