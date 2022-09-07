##########    1. dict values 
# dict[key] = values

my_dict = { 
    "brand" : "Mercedes", 
    "Model" : "G Class", 
    "year" : 1964 
}

my_dict["year"] = 2022


##########   2. update dict : this method wil update the dict with the items from the given argument
my_dict.update({"Price" : 99999})
print(my_dict)