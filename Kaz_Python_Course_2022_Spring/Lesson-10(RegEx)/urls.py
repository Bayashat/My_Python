import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")


sub_url = pattern.sub(r"\1\2", urls)
print(sub_url)

'''
matches = pattern.finditer(urls)
for match in matches:
    print(match.groups())
'''
