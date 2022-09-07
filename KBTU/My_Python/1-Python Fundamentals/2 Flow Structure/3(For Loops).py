'''             For loops
    语句:
    for 临时变量 in 可迭代对象:
      重复执行的代码1
      重复执行的代码2
'''
              ###   1.Python For Loops
# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# The for loop does not require an indexing variable to set beforehand.
--------------------------------------------------------------------------------------------------
              ##    2.Looping Through a String
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)
---------------------------------------------------------------------------------------------------
              ##    3.The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
-------------------------------------------------------------------------------------------------
              ##    4.The continue Statement
# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
--------------------------------------------------------------------------------------------------
              ##    5.The range() Function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)  # 0，1，2，3，4，5.

----------------------------------------------------------------------------------------------------------
              ##    6.The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:
    # range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)  # 2，3，4，5.

------------------------------------------------------------------------------------------------------------
              ##    7.The range() function defaults to increment the sequence by 1,
    # however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)  # 2，5，8，11.......

------------------------------------------------------------------------------------------------------------
              ##    8.Else in For Loop
# Else 是当循环正常结束后执行的代码.
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

在 For-Else 使用 break 终止循环不会执行Else
在 For-Else 使用 Continue 退出循环会执行else
-------------------------------------------------------------------------------------------------------------
              ##    9.Nested Loops
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
-------------------------------------------------------------------------------------------------------------
            ##    10.The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
