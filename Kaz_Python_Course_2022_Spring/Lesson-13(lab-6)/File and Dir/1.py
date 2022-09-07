import os


path = os.getcwd()

print("Only directories: ")

for file in os.listdir(path):  # qwer, 1.py
    if os.path.isdir(file):
        print(file)

print("\nOnly files: ")
for file in os.listdir(path):  # qwer, 1.py
    if not os.path.isdir(file):
        print(file)
       
print("\nAll files and dirs: ")
print(os.listdir())