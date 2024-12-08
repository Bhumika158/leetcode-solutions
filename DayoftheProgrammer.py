"""Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

Divisible by 400.
Divisible by 4 and not divisible by 100."""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    ## Time: O(1) and Space: O(1)
    # y=int(year)
    # if 1700<=y<=1917:
    #     if y%4==0:
    #         return f"12.09.{year}"
    #     else:
    #         return f"13.09.{year}"
    # elif 1919<=y<=2700:
    #     if (y%400==0) or (y%4==0 and not y%100==0):
    #         return f"12.09.{year}"
    #     else:
    #         return f"13.09.{year}"
    # else:
    #     return f"26.09.{year}"

    ## Time: O(1) and Space: O(1)
    # y=int(year)
    # if 1700 <= y <= 1917:
    #     if y % 4 == 0:
    #         Feb=29
    #     else:
    #         Feb=28
    # elif 1919 <= y <= 2700:
    #     if (y%400==0) or (y%4==0 and not y%100==0):
    #         Feb=29
    #     else:
    #         Feb=28
    # else:
    #     Feb=15
    #
    # jan_to_aug=31+Feb+31+30+31+30+31+31
    # date= 256-jan_to_aug
    # return f"{date}.09.{year}"

    ##Time: O(1) Space: O(1)
    y=int(year)
    if y == 1918:
        return "26.09.1918"
    elif (y < 1918 and y % 4 == 0) or \
            (y > 1918 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))):
        return f"12.09.{y}"
    else:
        return f"13.09.{y}"
print(dayOfProgrammer("2017"))