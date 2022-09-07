######## 1. Accessing items-1 : 
import this


my_dict = { "brand" : "Mercedes", "Model" : "G Class", "year" : 1964 }

print(my_dict["Model"]) # G class
# print(my_dict["abcd"]) # error


####### 2.1 get(key)

print(my_dict.get("brand")) # Mercedes
print(my_dict.get("abcd"))  # None

#####   2.2 get(key, value) : ifn the key does not exists, returns the value
print(my_dict.get("abcd", 55))  # 55


########  3. Keys() : get all the keys in Dict
print(my_dict.keys())  # dict_keys(['brand', 'Model', 'year'])

######3 4. values ()
print(my_dict.values()) # dict_values(['Mercedes', 'G Class', 1964])

######### 5. items()
print(my_dict.items()) # dict_items([('brand', 'Mercedes'), ('Model', 'G Class'), ('year', 1964)])

#######  6. check if key exists :
my_dict = { "brand" : "Mercedes", "Model" : "G Class", "year" : 1964 } 

if "Model" in my_dict:
    print("YESSSSS") 




      
