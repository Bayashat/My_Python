from math import tan, pi

n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))

Area = int(n_sides * (s_length**2) / (4*tan(pi / n_sides)))

print(f"The area of the polygon is: {Area}")