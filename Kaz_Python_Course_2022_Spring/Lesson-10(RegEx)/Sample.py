import re

s = "hello"
text_to_search = '''
qwert is fun
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com
coreyms*com
coreyms-com

321-555-1234
123.555.1234
123*555*1234

800-555-1234
900-555-1324

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T


cat 
mat
pat
bat
'''
'''
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")  
matches = pattern.findall(text_to_search)

#pattern = re.compile(r"\.")
#pattern = re.compile(r"coreyms\.com")  # coreyms.com
#pattern = re.compile(r"\d\d\d[-.]555[.-]\d\d\d\d")  
#pattern = re.compile(r"\d\d\d\.555\.\d\d\d\d")  # 123.555.1234
#pattern = re.compile(r"[89]00-555-\d\d\d\d")  # 800-555-1234 or 900-555-1324
#pattern = re.compile(r"[1-5]") # 1 2 3 4 5
#pattern = re.compile(r"\.")
#pattern = re.compile(r"\wat") 
# pattern = re.compile(r'\d{3}[.-]\d{3}[-.]\d{4}')  # 
# pattern = re.compile(r"[^c]at") # mat pat bat

#matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
'''

txt = "START a sentence and then "
pattern = re.compile(r"Start", re.IGNORECASE) # re.I
#matches = pattern.match(txt)
matches = pattern.search(txt)
print(matches)
 