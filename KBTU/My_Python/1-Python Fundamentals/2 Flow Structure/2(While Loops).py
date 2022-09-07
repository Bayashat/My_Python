                    ## 1.Python Loops

# Python has two primitive loop commands:
while loops
for loops
-----------------------------------------------------------------------------------------------------------------
                    ## 2.the WHILE Loop

    # While 语句基本语法:
'''
  初始条件设置 - 通常是重复执行的 计数器
  
  while 条件(判断 计数器 是否达到 目标次数):
    条件满足时, 做的事情1
    条件满足时, 做的事情1
    .......
'''
# With the while loop we can execute a set of statements as long as a condition is true.
# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
# Note: remember to increment i, or else the loop will continue forever.
---------------------------------------------------------------------------------------------------------------
                  ## 3.The break Statement
# With the break statement we can stop the loop even if the while condition is true:(终止此循环)
# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
-----------------------------------------------------------------------------------------------------------
              ## 4.The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next(退出当前循环，执行下一次循环)
# !!!!!注意!!!!  Continue之前一定要加 计数器的变化.否则会进入死循环
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
-------------------------------------------------------------------------------------------------------------
              ## 5.The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
-----------------------------------------------------------------------------------------------------------------------
                  ##6. While-else with "continue" or "break"

当在 while else 循环使用 Continue 的话，else 里的语句会被执行.

而在 while else 使用 Break 的话，else 里的语句不会被执行.