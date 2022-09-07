my_tuple = ("apple", "banana", "cherry")

(a, b, c) = my_tuple

print(a) # banana
print(b) # banana
print(c) # cherry

#############################

# Asterix - 1

t = ("apple", "banana", "cherry", "Limon", "Melon")
(a, b, *c) = t
print(a) # apple
print(b) # banana
print(c) # ['cherry', 'Limon', 'Melon']


# Asterix-2

t = ("apple", "banana", "cherry", "Limon", "Melon")
(a, *b, c) = t
print(a) # apple
print(b) # ['banana', 'cherry', 'Limon']
print(c) # Melon