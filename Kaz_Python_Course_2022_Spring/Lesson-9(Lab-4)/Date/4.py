from datetime import datetime, time

date1 = datetime.strptime('2000-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.strptime('2022-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

def date_diff(date1, date2):
    t = date2 - date1

    return t.days * 24 * 3600 + t.seconds

print(date_diff(date1, date2))