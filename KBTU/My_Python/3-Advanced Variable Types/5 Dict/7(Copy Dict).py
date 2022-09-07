"""
                  < 7 > Copy Dict
"""


#                   1.Make a copy of a dictionary with the copy() method:

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = this_dict.copy()
print(mydict)
# -------------------------------------------------------------------------------------------------------------------
#                   2.Another way to make a copy is to use the built-in function dict().

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
my_dict = dict(this_dict)
print(my_dict)

