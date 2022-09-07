#      1. abs(int)	

# Returns the absolute value of a number

print(abs(-1))  # 1
print(abs(-1.4)) # 1.4
print(abs(1.3))  # 1.3

def my_abs(num):
    if num < 0:
        return num * -1
    return num

print(my_abs(-55)) #55