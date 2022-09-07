# if you have an python object, you can convert it to a JSON string by using 
# json.dumps()

import json

# a python object(dict)
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
data = json.dumps(x)
print(data)  # {"name": "John", "age": 30, "married": true, "divorced": false,"children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}


data = json.dumps(x, indent=3)
print(data)


##########  Example : Convert Python to JSON strings and print the values:
print(json.dumps({"name":"John","age":30})) # '{"name": "John", "age": 30}'
print(json.dumps(["apple", "banana", "cherry"])) # '["apple", "banana", "cherry"]'
print(json.dumps(("apple", "banana", "cherry"))) # '["apple", "banana", "cherry"]'
print(json.dumps("hello")) # 'hello'
print(json.dumps(42))  # "42"
print(json.dumps(31.76)) # "31.76"
print(json.dumps(True)) # true
print(json.dumps(None)) # null


########  Using the seperators : 
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

data = json.dumps(x, indent=3, separators= (". ", " = "))  # . бұл екі обьектіні бөлетін символ,  = бұл әр key:value дің арасын бөлетін символ
print(data)
'''
{
   "name" = "John".
   "age" = 30.
   "married" = true.
   "divorced" = false.
   "children" = [
      "Ann".
      "Billy"
   ].
   "pets" = null.
   "cars" = [
      {
         "model" = "BMW 230".
         "mpg" = 27.5
      }.
      {
         "model" = "Ford Edge".
         "mpg" = 24.1
      }
   ]
}
'''

# Sort the JSON
data = json.dumps(x, indent=3, sort_keys=True)
print(data)