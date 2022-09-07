""""
Enter a number, and you should print such row stars
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""
        ###  1. For loop version:

n = int(input("How much row? "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


'''
        ###  2. While loop version:
i = 0
while i < n:
    j = 0
    while j <= i:
        print("*", end = " ")
        j += 1
    i += 1
    print()
'''
