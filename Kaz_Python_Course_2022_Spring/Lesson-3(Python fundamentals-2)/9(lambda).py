# a lambda function is a small anonyms function

# syntax: lambda arguments : expression

def fn1():
    return 200
print(fn1()) 

fn2 = lambda : 100

print(fn2()) # 100


###########  <Example-1> : calculate a+b
# use function : 
def add(a,b):
    return a+b

result = add(10,20) # 30

# 2) use lambda :
fn = lambda a,b : a+b
print(fn(1,2)) # 3
print((lambda a,b : a+b) (10, 20))  # 30