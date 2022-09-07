"""
                  < 4 > Iterate Tuples
"""
#             1.Loop Through a Tuple

this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
    print(x)
# -------------------------------------------------------------------------------------------------------------
#             2.Loop Through the Index Numbers

this_tuple = ("apple", "banana", "cherry")
for i in range(len(this_tuple)):
    print(this_tuple[i])
# -------------------------------------------------------------------------------------------------------------------
#             3.Using a While Loop

this_tuple = ("apple", "banana", "cherry")
i = 0
while i < len(this_tuple):
    print(this_tuple[i])
    i = i + 1
# -------------------------------------------------------------------------------------------------------------------
