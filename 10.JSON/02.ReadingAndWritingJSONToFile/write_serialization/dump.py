import json

# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}

with open("sampledump.json", 'w') as outputFile:
    json.dump(dictionary, outputFile, indent=5)

# Because dump() can take a filepointer arg to specify the outputfile, naturally this method can directly
# write a dictionary to file without creating a json object.

