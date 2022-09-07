# Once a set is created, you cannot change its items, but you can add new items
my_set = {"apple", "banana", "Cherry"}


                #######   1. add() method : only add the single elements
my_set.add("Orange")
print(my_set)

                ####  2. Update() method : add the collections
s2 = {"mango", "Limon", "Kiwi"}
my_set.update(s2)
print(my_set)       # {'Limon', 'banana', 'Cherry', 'Kiwi', 'Orange', 'mango', 'apple'}


                ##### 3. Update() : add any iterable collections
l = ["KBTU", "AITU"]
my_set.update(l)
print(my_set)  # {'AITU', 'apple', 'mango', 'Cherry', 'banana', 'Orange', 'Limon', 'KBTU', 'Kiwi'}