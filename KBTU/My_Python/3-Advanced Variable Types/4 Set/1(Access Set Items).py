"""
                    < 1 > Access Set items
"""
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
#     by using the in keyword.
# -------------------------------------------------------------------------------------------------------------------------------------------
#                    1.Loop through the set, and print the values:

this_set = {"apple", "banana", "cherry"}

for x in this_set:
  print(x)
# --------------------------------------------------------------------------------------------------------------------------------------------
#                   2.Check if "banana" is present in the set:

this_set = {"apple", "banana", "cherry"}

print("banana" in this_set)  # True