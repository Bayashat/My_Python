import math

def count_volume(radius):
    volume = (4 / 3) * math.pi * radius**3
    print(f"Volume of sphere is {volume:.2f}")

radius = float(input())
count_volume(radius)
