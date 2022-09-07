x = int(input())
c = input()

if c == 'k':
    y = int(input())
    number = x / 1024
    print(f'{number:.{y}f}')
else:
    print(x * 1024)
