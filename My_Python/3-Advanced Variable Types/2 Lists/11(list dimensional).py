"""
                < 12 > List dimensional
"""

school_names = [['KBTU', "IITU"],
                ['ATU', 'AITU', 'KAZGU'],
                ['AGU', 'ENU']]

x = [['KBTU', 'IITU'], ['ATU', ['AITU'], ['KAZGU']]]

print(school_names[1])  # ['ATU','AITU','KAZGU']
print(school_names[1][1])  # AITU
print(school_names[1][1][1])  # 'I'
