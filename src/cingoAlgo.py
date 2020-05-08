# Python program to find the next time cinco de mayo will fall on a tuesday

import datetime
import calendar

"""
the datetime.strptime() class method creates a datetime object from a 
string representing a date and time and a corresponding format string.

A datetime object is a single object containing all the information 
from a date object and a time object.

datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
The year, month and day arguments are required.




"""

# tacotuesday variable
# format string with strptime so 05/05/yyyy
# %d Day of the month as a zero-padded decimal number.
# %m Month as a zero-padded decimal number.
# %Y Year with century as a decimal number.
# .weekday() returns day of the week as an int (1=Mon, 2=Tues etc)
# return weekday as a name with calendar.day_name


def findDay(cincodemayo):
    tacotuesday = datetime.datetime.strptime(cincodemayo, '%d %m %Y').weekday()
    return (calendar.day_name[tacotuesday])  # Tuesday


cincodemayo = '05 05 2020'
print(findDay(cincodemayo))
cincodemayo = '05 05 2021'
print(findDay(cincodemayo))
cincodemayo = '05 05 2022'
print(findDay(cincodemayo))
cincodemayo = '05 05 2023'
print(findDay(cincodemayo))
cincodemayo = '05 05 2024'
print(findDay(cincodemayo))
cincodemayo = '05 05 2025'
print(findDay(cincodemayo))
cincodemayo = '05 05 2026'
print(findDay(cincodemayo))
