# Regular expression
import re

pattern1 = "cat"
pattern2 = "bird"

string = "dog runs to cat"
print(pattern1 in string)  # True
print(pattern2 in string)  # False

pattern1 = "cat"
pattern2 = "bird"

string = "dog runs to cat"
print(re.search(pattern1, string))
print(re.search(pattern2, string)) # None


# 1. [] бірнеше символды іздеуге 
# Multiple patterns : ran or run
ptn = r"r[au]n"  # run or ran
print(re.search(ptn, string))

# 2. 
print(re.search(r"r[A-Z]n", "dog rWns to me"))  # rAn, rBn, rHn
print(re.search(r"r[a-z]n", "dog runs to me"))  # ren, rwn, ron,
print(re.search(r"r[0-9]n", "dog r2ns to me"))  # r1n, r5n, r9n, r2n
print(re.search(r"r[0-9a-zA-Z_]n", "dog runs to me")) # r5n, ren, rSn, r_n, 


# 3. Special characters:

            # 1) Numbers:
# \d decimal digits
print(re.search(r"r\dn", "run r4n"))
# \D : any non-decimal digits
print(re.search(r"r\Dn", "run r4n"))

            # 2) White space
# \s : any white space [\t\n\r\f\v]
print(re.search(r"r\sn", "r\nn r4n"))  # r\nn
# \S : opposite to \s : any non-white space
print(re.search(r"r\Sn", "r\nn r4n"))  # r4n

            # 3) Барлық әріптер сандар и _
# \w [a-zA-Z0-9]
print(re.search(r"r\wn", "r\nn r4n")) # r4n
# \W : opposite to \w:
print(re.search(r"r\Wn", "r\nn r4n")) # r\nn

            # 4) Empty string :
# \b : empty string(only at the start or end of the word):
print(re.search(r"\bruns\b", "dog runs to cat"))
#\B: empty string(but not at the start or end of the word):
print(re.search(r"\Bruns\B", "dog runs to cat"))

            # 5)special charachters:
# \\ : match \
print(re.search(r"runs\\", "runs\ to me"))

# . : match anything (except \n):
print(re.search(r"r.n", "r[ns to me]"))

            # 6) Beginning Ending:
# ^ : match line begiining :
print(re.search(r"^dog", "dog runs to cat"))

# $ : match line ending:
print(re.search(r"cat$", "dog runs to cat"))

            # 7) ?
# ? : may or may not occur :
print(re.search(r"Mon(day)?","Monday"))
print(re.search(r"Mon(day)?","Mon"))

            # 8) : Multiple line
string = 
dog runs to cat.
I run to dog.

print(re.search(r"^I", string)) 
print(re.search(r"^I", string, flags=re.M)) 

            # 9) : *
# * : occur 0 or more times
print(re.search(r"ab*", "a"))
print(re.search(r"ab*", "abbbb"))

            # 10) +
# +: occur 1 or more times:
print(re.search(r"ab+", "a"))  # None
print(re.search(r"ab+", "abbbb"))

            # 11) {}
# {n,m}: occur n to m times
print(re.search(r"ab{2,10}", "a"))   # None
print(re.search(r"ab{2,10}", "abbbbb"))

            # 12 Group
match = re.search(r"(\d+), Date: (.+)", "ID: 021253, Date: Feb/12/2020")
print(match.group()) # 021253 Feb/12/2020
print(match.group(1)) # 021253
print(match.group(2)) # Feb/12/2020

match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021253, Date: Feb/12/2020")
print(match.group("id")) # 021253
print(match.group("date")) # Feb/12/2020

            # 13. Findall
print(re.findall(r"r[ua]n", "run ren ran")) # ['run', 'ran']

# | :  or
print(re.findall(r"(run|ran)","run ren ran")) # ['run', 'ran']


            # 14. Replace
# re.sub 
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))  # dog catches to cat

            # 15. Split :
print(re.split(r"[,;\.]", "a;b,c.d;e")) # ['a', 'b', 'c', 'd', 'e']

            # 16. compile 
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog runs to cat"))
