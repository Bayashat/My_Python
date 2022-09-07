                  ## 1.Python supports the usual logical conditions from mathematics:

"""
Equals:                 a == b
Not Equals:             a != b
Less than:              a < b
Less than or equal to:  a <= b
Greater than:           a > b
Greater than or equal to: a >= b
"""
---------------------------------------------------------------------------
                ## 2.If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

  ------------------------------------------------------------------------
                ## 3.Elif
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

-----------------------------------------------------------------------------------------------------------------------
                ## 4.Else
#  The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

------------------------------------------------------------------------------------------------------------------------
                  ## 5.Simply if

if (age>=18) and (age<=60)  can simply to :  if 18<=age<=60
----------------------------------------------------------------------------------------------------------------
            ## 6.Short Hand If

# If you have only one statement to execute, you can put it on the same line as the if statement.
# One line if statement:
if a > b: print("a is greater than b")

----------------------------------------------------------------------------------------------------------------
          ## 7.Short Hand If ... Else
变量 = 条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
a = 2
b = 330
print("A") if a > b else print("B")
# !!! This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

-----------------------------------------------------------------------------------------------------------
                    ## 8.And
# The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

----------------------------------------------------------------------------------------------------------------
                    ## 9.Or
# The or keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

--------------------------------------------------------------------------------------------------------------------
                  ## 10.Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

---------------------------------------------------------------------------------------------------------------
                  ## 11.The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass
----------------------------------------------------------------------------------------------------------------