#                       1. Public Operation / 公共方法
"""
1.  +        Join(合并)         String, List, Tuple

2.  *        Copy(复制)         String, List, Tuple

3.  in       元素是否存在       String, List, Tuple， Dict

4.  Not in   元素是否不存在     String, List, Tuple， Dict
"""
#                   1 : JOIN +
str1 = 'aa'
str2 = 'bb'

list1 = [1,2]
list2 = [10,20]

t1 = (1,2)
t2 = (10,20)

dict1 = {'name': 'issac'}
dict2 = {'age':18}

print(str1+str2)    # aabb
print(list1+list2)  # [1,2,10,20]
print(t1+t2)        # (1,2,10,20)
# print(dict1+dict2)  # error.  字典不支持合并

# ---------------------------------------------------------------------------------
#                   2: COPY *
str1 = 'a'
list1 = ['hello']
t1 = ('word',)

print(str1*5)       # aaaaa
print(list1*5)      # ['hello', 'hello', 'hello', 'hello', 'hello']
print(t1*5)         # ('word', 'word', 'word', 'word', 'word')

