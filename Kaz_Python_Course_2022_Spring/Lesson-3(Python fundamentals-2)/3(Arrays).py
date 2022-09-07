# !!! NOte : Pythn does not have built-in support for Arrays, but Python Lists can be used instead

                # 1. Create an array:
cars = ["BMW", "Porsche", "Audi"]

                # 2. Access the Elements:
x = cars[1]
print(x)  # Porsche

                # 3. Modify the value of Array:
cars[2] = "Ferrary"  
print(cars)    

                # 4. The length of Array:
# Use the len() method
x = len(cars) 
print(x) # 3

                # 5. Lopping Array :
print(cars)

# Exercise : for every car in Array, insert the number 2 at the end
for i in range(len(cars)):
    cars[i] += "2"

print(cars)  # ['BMW2', 'Porsche2', 'Ferrary2']

                # 6. Adding Array elements 
# add a new car named "Mercedes" to our Array
cars.append("Mercedes")
print(cars)  # ['BMW2', 'Porsche2', 'Ferrary2', 'Mercedes']

                # 7. Removing array elements:
# Delete the first element in array 

#    1. pop(index) : delete by index
cars.pop(0)
print(cars) #['Porsche2', 'Ferrary2', 'Mercedes']

#    2. remove(element)
cars.remove("Porsche2")
print(cars)  # ['Ferrary2', 'Mercedes']



                        # 8. Array Methods :
clear()          Remove all the elements from the list
copy()           returns a copy of the list
count(value)          returns the numbers of elements with specified value
reverse()
sort()
