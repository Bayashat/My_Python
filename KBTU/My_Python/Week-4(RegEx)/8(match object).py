'''
re.RegexObject
re.compile() 返回 RegexObject 对象。

re.MatchObject
group() 返回被 RE 匹配的字符串。

start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置

'''

                                ### 8.Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.


                                ## 8.1 match.group()
  # The group() method returns the part of the string where there is a match.

import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())
else:
  print("pattern not found")

print(match.start()) # 2
print(match.end())   # 8
print(match.span())  # (2,8)
# Output: 801 35

'''
-----------------------------------------------------------------------------------------------------------------------------------------------
'''
                                        ### # Ex-1: Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)     # <re.Match object; span=(5, 7), match='ai'>

.span()       returns a tuple containing the start-, and end positions of the match.
.string       returns the string passed into the function
.group()      returns the part of the string where there was a match

