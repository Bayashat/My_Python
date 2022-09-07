"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3746#1
    Задача №3746. Замена внутри фрагмента
Input: In the hole in the ground there lived a hobbit
Output: In the Hole in tHe ground tHere lived a hobbit
"""

s = input()

a = s[:s.find('h') + 1]  # In th
b = s[s.find('h') + 1:s.rfind('h')]  # e hole in the ground there lived a
c = s[s.rfind('h'):]  # hobbit

s = a + b.replace('h', 'H') + c
print(s)


"""
s = input()
a = s.find('h')
b = s.rfind('h')
s = s.replace('h', 'H')
s = s[:a] + 'h' + s[a+1:]
s = s[:b] + 'h' + s[b+1:]
print(s)
"""