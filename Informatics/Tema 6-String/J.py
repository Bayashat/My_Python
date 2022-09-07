"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3744#1
    Задача №3744. Замена подстроки
Input: 1+1=2
Output: one+one=2
"""

s = input()

s = s.replace("1", 'one')
print(s)

# print(input().replace('1', 'one'))