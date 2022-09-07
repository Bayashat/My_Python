# Ahd sdfjn, jafjd.  space, common, dot
# Ahd:sdfjn::jafjd:

import re

str = input()

str2 = re.sub(r"[\s,.]", ":", str)
# str2= re.sub(r"(\s|,|\.)", ':', str)
print(str2)
