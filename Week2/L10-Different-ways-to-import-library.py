import calendar

print(calendar.month(2024, 8))
#print entire 2026 year calendar
print(calendar.calendar(2026))

#different ways to import specific functions
from calendar import *
print(calendar(2026))
print(month(2025, 10))
#import specific functions
from calendar import calendar, month
print(calendar(2024))
print(month(2025, 10))
#import with alias
import calendar as c
print(c.month(2024, 8))

from calendar import month as m
print(m(2025, 10))