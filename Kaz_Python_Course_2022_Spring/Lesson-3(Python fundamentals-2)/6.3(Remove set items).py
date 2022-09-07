'''               ####  1. Remove() : remove the specified value, if doesn't exist : error
my_set = {10, 20, 30, 40, 50}

my_set.remove(10) 
print(my_set)  # {20,30,40,50}

my_set.remove(100) # error

                    ###  2. discarda() : remove the specified value
my_set.discard(20)
print(my_set)  # {30, 40, 50}

my_set.discard(100) 
'''
                    #### 3. pop() : randomly delelts, and returns that element : delete the last element in set, but remember that the set is unordered, so you will not know that what item that gets removed
my_set = {10, 20, 30, 40, 50}
x = my_set.pop()
print(x)


                    ##### 4. clear()

                    ###### 5. del()
# the del keyword will delete the set completely
del my_set
print(my_set) # error