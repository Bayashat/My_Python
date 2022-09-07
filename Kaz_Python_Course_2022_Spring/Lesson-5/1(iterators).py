######   Iterable object : List, tuple, dict, and sets, string 

                ## <1> Iterators
# All these objects have a iter() method 

# 1) return an iterator from a tuple, and print each value:
my_tuple = ("apple", "banana", "cherry")
my_it = iter(my_tuple) # StopIteration

print(next(my_it))
print(next(my_it))
print(next(my_it))


# 2) strings are also iterable objects 
s = "banana"
my_it = iter(s)
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))

        # <2> Lopping through an iterator: The for loop actually creates an iterator object and executes the next() method for loop
my_tuple = ("apple", "banana", "cherry")

for x in my_tuple:
    print(x)

for i in s:
    print(i)