#   Parse JSON - convert from JSON to Python
# json.loads()   # The result will be a python dict


# Example-1: 
import json

x = '{ "name" : "JOhn", "age" : 30, "city" : "New York" }'
# parse x :

data = json.loads(x)
print(data)