##############    10.Special Sequences

'''
1. \A	    匹配字符串开始
            Returns a match if the specified characters are at the beginning of the string	"\AThe"


2. \b	    匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
            Returns a match where the specified characters are at the beginning or at the end of a word
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
            r"ain\b"
             \b 匹配的是单词的边界   : \bmaster\b 就仅匹配有边界的master单词。


3. \B	    匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
            Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
            r"ain\B"


4. \d	    匹配任意数字，等价于 [0-9]。
            Returns a match where the string contains digits (numbers from 0-9)	"\d"
             \d，d即digit数字的意思，等价于[0-9]


5.\D	    	匹配任意非数字
            Returns a match where the string DOES NOT contain digits	"\D"


	        匹配任意空白字符，等价于 [\t\n\r\f]。
 6. \s       Returns a match where the string contains a white space character	"\s"
            \s快捷方式可以匹配空白字符，比如空格，tab、换行等


7. \S	    匹配任意非空字符
            Returns a match where the string DOES NOT contain a white space character	"\S"


8. \w	    匹配数字字母下划线
            Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
             \w 可以与任意单词字符匹配。 

9. \W	    匹配非数字字母下划线
            Returns a match where the string DOES NOT contain any word characters	"\W"


10. \z      匹配字符串结束


11. \Z	    匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
            Returns a match if the specified characters are at the end of the string	"Spain\Z"

12. \G      匹配最后匹配完成的位置。

13. \n, \t..         匹配一个换行符。匹配一个制表符, 等

14. \1...\9	        匹配第n个分组的内容。

15. \10	        匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
'''