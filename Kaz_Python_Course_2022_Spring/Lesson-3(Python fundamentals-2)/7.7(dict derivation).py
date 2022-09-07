###############3   <1>
## create a dict : key is 1-5 , values are such number's  square
## {1:1, 2 : 4, 3:9}

dict1 = {i : i**2 for i in range(1,6)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

##############  <2> : 
l1 = ['name', 'age', 'id']
l2 = ["Tom", 20, 1745]

dict1 = {l1[i] : l2[i] for i in range(3)}
print(dict1) # {'name': 'Tom', 'age': 20, 'id': 1745}



#########  <3>  : needs a dict of number > 200
counts = {'MBP' : 268, "HP" : 125, 'DELL' : 201, 'Lenovo' : 199, "acer" : 99}

dict1 = {key : value for key,value in counts.items() if value > 200}
print(dict1)   # {'MBP': 268, 'DELL': 201}