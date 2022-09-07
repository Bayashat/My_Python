#############       11.Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

'''

1. [Pp]ython	    匹配 "Python" 或 "python"

2. rub[ye]	        匹配 "ruby" 或 "rube"

3. [aeiou]	        匹配中括号内的任意一个字母
	                Returns a match where one of the specified characters (a, r, or n) are present

4. [0-9]	    匹配任何数字。类似于 [0123456789]
                Returns a match for any digit between 0 and 9

5. [a-z]	    Returns a match for any lower case character, alphabetically between a and z
                匹配任何小写字母

6. [A-Z]	    匹配任何大写字母

7. [a-zA-Z0-9]	    匹配任何字母及数字

8. [^aeiou]	    除了aeiou字母以外的所有字符
    	        Returns a match for any character EXCEPT a, e,i,o,u.

9. [^0-9]	    匹配除了数字外的字符               


10. [0-5][0-9]	    Returns a match for any two-digit numbers from 00 and 59

11. [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case

12.[+]	            In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string



'''