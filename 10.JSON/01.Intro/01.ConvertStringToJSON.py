import json

# JSON string
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'

# Convert json to python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print()

# Convert python dict to JSON
json_obj = json.dumps(employee_dict, indent=4)
print(json_obj)
print(type(json_obj))

json_obj1 = json.dumps(employee)
print(json_obj1)

