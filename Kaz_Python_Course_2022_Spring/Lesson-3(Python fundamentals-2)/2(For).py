'''
    for (i) in (Тізбек):
        ...
        ...
'''

                # 1. For lopps
# print each fruit in a fruit list
fruits = ["Apple", "Banana", "Lemon"]

for x in fruits:
    print(x)

                # 2. Lopping through a String :
# "Kazakhstan"
for i in "Kazakhstan": # K a z a k h s t a n
    print(i, end = " ")

                # 3. The break statement
for i in fruits:   # "Apple"
    if i == "Banana":
        break
    print(i)

                # 4. The continue statement
for i in fruits:   # "Apple", "Lemon"
    if i == "Banana":
        continue
    print(i)   

                # 5. The range() function
# автоматом 0-ден бастайды
# range(6) :  0-5     range(1,6) - 1-5
for i in range(1,5): # 1 2 3 4
    print(i)

# range(2,30,3) increment the sequence with 3 : 2 5 8 ... 29
for i in range(2,30,3):
    print(i, end = ' ')

                # 6. Nested loop :
adj = ["red", "Yellow", "Purple"]
fruits = ["Apple", "Banana", "Lemon"]

for x in adj :
    for y in fruits:
        print(x,y)

                # 7. Pass statement
# For loops can not be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error
for x in [0,1,2]:
    pass