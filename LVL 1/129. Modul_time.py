import time
import sys

print()
print(time.time())
print(time.localtime(time.perf_counter()))

import calendar

print(calendar.month(1993,8))
print(calendar.month(1993,8).setfirstweekday(6))
