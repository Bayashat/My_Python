# in Python, the function used "yield" called Generator

# Ex-1:
def f():
    yield 1
    yield 2
    yield 3

print(f()) # <generator object f at 0x000002BAAC619A10>

# to call the generator:
it = f()
print(next(it)) # 1 
print(next(it)) # 2 
print(next(it)) # 3
# print(next(it)) # StopIteration

# Ex-2:
def f(n):
    a = 0
    b = 1
    for i in range(0,n):
        yield a+b
        b = b +1

it = f(10)
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # 4
print(next(it)) # 5
print(next(it)) # 6
print(next(it)) # 7
print(next(it)) # 8
