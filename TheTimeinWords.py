"""Given the time in numerals we may convert it into words, as shown below:
5:00 : five o' clock
5:01 : one minute past 5
5:10 : ten minutes past 5
5:15 : quarter past 5
5:30 : half past 5
5:40 : twenty minutes to 6
5:45 : quarter to 6
5:47 : thirteen minutes to 6
5:28 : twenty eight minutes past 5
At ,minutes=0 use o' clock. For 1<=minutes<=30, use past, and for 30<minutes use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty"]
    def literal(n):
        if 1 <= n < 10:
            return ones[n]
        elif 10 <= n < 20:
            if n == 10:
                return "ten"
            return teens[n - 10]
        elif 20 <= n < 60:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    if m==0:
        return f"{literal(h)} o' clock"
    elif 1 <= m <= 30:
        if m == 15:
            return f"quarter past {literal(h)}"
        elif m == 30:
            return f"half past {literal(h)}"
        elif m == 1:
            return f"one minute past {literal(h)}"
        else:
            return f"{literal(m)} minutes past {literal(h)}"
    else:
        mins_to_next_hour = 60 - m
        next_hour = h + 1 if h < 12 else 1
        if mins_to_next_hour == 15:
            return f"quarter to {literal(next_hour)}"
        elif mins_to_next_hour == 1:
            return f"one minute to {literal(next_hour)}"
        else:
            return f"{literal(mins_to_next_hour)} minutes to {literal(next_hour)}"


print(timeInWords(5,1))