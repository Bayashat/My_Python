            ### 1. Access tuple items
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # banana

            ###  2.Negative indexing
print(my_tuple[-1]) # cherry

            ### 3. Range
print(my_tuple[: 2])
print(my_tuple[1 : ])
print(my_tuple[1:2])

            ### 4. Change tuple:
l = list(my_tuple)
l[1] = 'Limon'
my_tuple = tuple(l)
print(my_tuple)  # ('apple', 'Limon', 'cherry')

            ##### 5. Add items
# convert to list and use the add item methods

        #####   6. Remove items
# convert to list and use the remove item methods

        #### 7. Delete tuple 
del my_tuple
