#               <1>
print("Hello world")

# string x = "apple"
x = 'Apple'

print("I have an " + x)

x = "Apple"
y = " is good"
z = x + y
print(z)

#       <2>
age = 18
print("My age is %d" %age)

name = "Ivan"
height = 170.5
print("My name is %s, my age is %d, my height is %.1f" %(name, age, height))
'''
%c ------ charcter  
%s ----- string
%d ----- integer
%f ----- float

'''



#                   <3>
#       "Pass is 50%"
number = 50
print("Pass is %d%%"%number)

#           <4>  f'text' {}
age = 18
name = "Ivan"
print(f"My name is {name}, my age is {age}")

height = 170.5
print(f"My name is {name}, my age is {age}, my height is {height:.2f}cm ")


#           <5> end
print("Hello", end = ",")
print("My name is Peter")