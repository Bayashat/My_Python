#  built-in has time and calendar modules
# time's all in second : from 1970.01.01

from cmath import pi
import time

ticks = time.time()

print(ticks)  #1644941336.9572678 / 3600 / 24 / 365 = 52 : 1970 + 52 = 2022

                ##### <1> Python Dates
import datetime

x = datetime.datetime.now()
print(x) # 2022-02-15 22:10:45.866325

from datetime import datetime
now = datetime.now()
print(now) # 2022-02-15 22:11:25.125209

print(now.day) # 15
print(now.month) # 2
print(now.year) # 2022

print(now.strftime("%Y:%m:%d %H:%M:%S")) # 2022:02:15


                ######### <2> Date output
# Return the yeaar and name of weekday
x = datetime.now()
print(x.year) # 2022
print(x.strftime("%A"))  # Tuesday


                ######### <3> creating Date objects:



                ####### <4> strftime method()

# 1: Display the name of the month:
x = datetime(2018, 6, 1)
print(x.strftime("%B")) # June
print(x.strftime("%A")) # Friday


'''
%a       weekday, short version
%A       weekday, full version

%w      weekday as a number 0-6, 0 is Sunday
%d      Day of month 01-31
%b      Month name, short
%B      Month name, full
%m      MOnths as number : 01-12
%y      Year, short
%Y      Year, full
%H      Hour 00-23
%I      Hour 00-12
%p      AM/PM
%M      Minute 00-59
%S      Second : 00-59
%f      Microsecond : 000000-999999
%z      UTC offset
%Z      Timezone
#j      Day number of year 001-366
#U      week number of year, Sunday as the first day of week : 00-53
#c      Local version of date and time







'''


