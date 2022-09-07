            ### 1. by index
t = ('aa', 'bb', 'cc', 'dd')
print(t[0]) # aa

            ### 2. index()
            # t.index(value)
print(t.index('bb')) # 1

            ### 3. count()
print(t.count('cc')) # 1

            ### 4.len
print(len(t)) # 4

            ### 5. 
t = ('aa', 'bb', 'cc', [10,20],  'dd')
t[3][0] = 50
print(t) # ('aa', 'bb', 'cc', [50, 20], 'dd')