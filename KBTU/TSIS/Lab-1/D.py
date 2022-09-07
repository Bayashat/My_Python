a = int(input())
c = input()

if c == 'k':
    b = int(input())
    d = a / 1024
    print(f'{d:.{b}f}')

else:
    print(a * 1024)