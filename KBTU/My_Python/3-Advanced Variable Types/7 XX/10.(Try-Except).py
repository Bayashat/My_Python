try:
    value = 10 / 0 # it's an error, but actually it's a "Zero division error"
    number = int(input("Enter a number: "))  # if we enter something that's not number, it will give us error
    print(number)
except ZeroDivisionError as err:
    print(err)

except ValueError: # when gives error, it will do
    print("invalid input")

