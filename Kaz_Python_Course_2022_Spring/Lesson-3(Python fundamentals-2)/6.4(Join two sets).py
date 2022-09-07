############   1. Join two sets
'''
You can use the union() method that returns a new set sontaining all items from both sets, or the update() method inserts all the items from one set to onother



'''

                ### 2. Union()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # {'a', 'b', 1, 2, 3, 'c'}

               #####   3. Update()
# The update() method inserts the items in s2 to s1:
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) # {'b', 1, 2, 3, 'c', 'a'}


                ##########  4. intersection_update() : keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)    # {'apple'}

                #########  5. intersection() method will return a new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)


                #### symmetric_difference_update() : Keep all, but not the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) 
print(x) # {'cherry', 'microsoft', 'banana', 'google'}

                ##### symmetric_difference() : return the new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) 