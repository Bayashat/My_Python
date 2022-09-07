"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3748#1
    Задача №3748. Удалить каждый третий символ
Input: Python
Output: yton
"""
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
