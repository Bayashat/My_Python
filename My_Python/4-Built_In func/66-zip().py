########################  66.zip()

'''

The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# Syntax:
zip(iterator1, iterator2, iterator3 ...)

iterator1, iterator2, iterator3 ...	    ----    Iterator objects that will be joined together

''''

# Ex-1: Join two tuples together:

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)       # (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

# Ex-2: If one tuple contains more items, these items are ignored:

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)       # (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))


# Ex-3:   
a = ['a', 'b', 'c', 'd']
index = [1, 2, 3]
c = (11, 22, 33, 55)

print(list(zip(a, index, c)))

for a, b, c in zip(a, index, c):
  print(f'{a} -> {b} -> {c}')


def my_zip():
  pass