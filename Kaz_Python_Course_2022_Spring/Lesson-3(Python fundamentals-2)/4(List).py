'''
collections : Жиын, Тізбек

there are 4 collecion data type in the Python:

1. List is a collecion which is ordered and changable. Allows duplicate members

2. Tuple is a collection which is ordered and unchangable.  Allows duplicate members

3. Set is a collection which is unordered and unindexid. No duplicate members

4. Dictionary is a collection which is unordered and changable. No duplicate members

'''

                        ### 1. List

My_List = ["Apple", "Cherry", "Banana"]
print(My_List)

                        ### 2. List items
# List items are indexed, the first item has index [0], the second has index [1] etc.

                        ### 3. List Length
# use the len() method

                        ### 4. List data types
x = ["Apple", "Cherry"]
y = [1, 3, 15, 48 ]
z = [True, False, True]
s = ["Abc", 15, True, "Male"]

                        ### 5. The List() constructor
# 1. Using the list() constructor to make a list
abc = list()
print(abc)  # []

# 2. Use the [] 
ZZZ = []
print(ZZZ)  # []

                        ### 6. Access the list 
print(x[1])  # Cherry
print(x[-2]) # Apple

Me = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(Me[2:5])  # ['cherry', 'orange', 'kiwi']
print(Me[:4])   # ['apple', 'banana', 'cherry', 'orange']
print(Me[3:])   # ['orange', 'kiwi', 'melon', 'mango']


                        ### 7. Loop the list :
#  1.
for i in Me :
    print(i)

# 2.
print(Me)

# 3. 
for i in range(len(Me)):
    print(Me[i])

# 4.
i = 0
while i < len(Me):
    print(Me[i])
    i += 1

# 5.
[print(x) for x in Me]



                        ### 8. Add List items
# 1. Append  : add the element at the end of list
l = [10, 20]
l.append(30) # [10,20,30]
l.append([77,88]) # [10,20,30 [77,88]]

# 2. Insert : list.insert(index, value)
l = [10, 20, 30]
l.insert(1, 50) # [10,50,20,30]


#  3. Extend list : list.extend(iterable object) : list, str
l = ["Apple", "Melon", "Banana"]
q = [10,20,30]
l.extend(q)
print(l) # ['Apple', 'Melon', 'Banana', 10, 20, 30]


                        #### 9. Search in List :
# 1. list.index(value, start, end)
# returns the index of the value, if not found, return error
l = [1, "Issac", 3.14, False]
num = l.index(3.14) # 2

#  2. Count() 
num = l.count(1) # 1

# 3. in / not in
# True / False

x = 3 in l  # False
y = 3.14 in l # True

                    #### 10. Remove list tems

# 1. list.remove(Value)
l = [10,20,30,40,50,60,70,80,90,100]
l.remove(30) 

# 2. list.pop(index)
num = l.pop(3) # 50

# 3. del list[index]
del l[0] 
del l   # []

# 4. clear()
#l.clear() # []


                        ### 11. Sort lists
# 1. Sort the list alphanumerically:
l = ["Apple", "Melon", "Banana"]
l.sort()
print(l) # Apple, Banana, Melon


# 2. Sort the list numerically
l = [100, 50, 65, 82, 23]
l.sort()
# print(l) # 23, 50, 65, 82, 100

# 3. Sort in descending order:
# list.sort(reverse = True)
l = [100, 50, 65, 82, 23]
l.sort(reverse=True)
print(l)   # [100, 82, 65, 50, 23]



#  4. sorted(list) : doesn't change the original list, sort the list and give it for the new list
l1 = [3,7,4,2,8,5,3]
l2 = sorted(l1)
print(l2) # [2, 3, 3, 4, 5, 7, 8]
print(l1) # [3, 7, 4, 2, 8, 5, 3]


#  5. Sort function

def myfunc(n):
    return abs(n-50)

l = [100,50,65,82,23]
l.sort(key = myfunc)

print(l) #[50, 65, 23, 82, 100]

#   6. Reverse order :
l.reverse()

#  7. Лист элементтерін тез кері ауыстыру :
l = [1,2,3,4,5]
x = l[::-1]
print(x) # [5,4,3,2,1]



                        #### 12.Join lists:
#    1. JOin two lists    
# using the + operator
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2 
print(list3) # ['a', 'b', 'c', 1, 2, 3]


#    2 Another way to join 2 lists by appending all items from l2 to l1, one by one
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1) # ['a', 'b', 'c', 1, 2, 3]


                            ### 13. List dimentonall:
# we are live in 3D life. 

school_names = [['KBTU', "IITU"],
                ['ATU', 'AITU', "KAZGU"],
                ['AGU', 'ENU']]

print(school_names[1]) # ['ATU', 'AITU', 'KAZGU']
print(school_names[1][1]) # AITU
print(school_names[1][1][1]) #  I


                            #### 14. List derivation
        ###  1. Simple list:
# (1.0) use the for :
list1 = []
for i in range(10):
    list1.append(i) 
print(list1) # 0-9

# (2.0) use whlile loop:
i = 0
while i < 10:
    list1.append(i)
print(list1)

# (3.0) Use list derivatoion :
list1 = [i for i in range(10)] 
print(list1) # 0-9

        ### 2. Conditional list:
# need a list with even numbers between 0-10
# Method-1 : use range steps:

list1 = [i for i in range(0,10,2)]
print(list1)

# Method-2 : use if statement
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)


            ### 3. Multile For list
# Need create such list : 
# [ (1,0) , (1,1), (1,2), (2,0), (2,1), (2,2)]

# our traditionally method
list1 = []
for i in range(1,3):
    for j in range(3):
        list1.append((i,j))
print(list1)

# new method :
list1 = [(i,j) for i in range(1,3) for j in range(3)]
print(list1)