                    #  1. The while loop

print(100)
print(100)
print(100)
print(100)
print(100)

i = 1
while i < 100:  
    print(100)
    i+=1
    
# Remember to increment i, or else the loop will continue forever.

                    # 2. The Break statement
# Условия : 3-ке келгенде осы циклді тоқтат
i = 1
while i < 6:  # 1 2 3
    print(i)
    if i == 3 :
        break
    i += 1

                    # 3. The Continue statement
# Условия : именно 3-ке келгенде оны экранға шығарма
i = 0
while i < 6:  # 1 2 4 5 6
    i += 1
    if i == 3:
        continue
    print(i)


   
