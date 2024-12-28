"""Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15hackos * (no,. of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine= 500 Hackos* (no.of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10000 Hackos."""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    ##Time: O(1), Space: (1)
    # if y1>y2:
    #     return 10000
    # elif y1==y2 and m1>m2:
    #     return 500*(m1-m2)
    # elif y1==y2 and m1==m2 and d1>d2:
    #     return 15*(d1-d2)
    # else:
    #     return 0

    ##Tuple Comparison: Time: O(1), Space: O(1)
    if (y1, m1, d1) <= (y2, m2, d2):
        return 0
    if y1>y2:
        return 10000
    if m1>m2:
        return 500*(m1-m2)
    return 15 * (d1-d2)


print(libraryFine(14,7,2018,5,7,2018))