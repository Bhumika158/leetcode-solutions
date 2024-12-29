"""A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2*d digits long or 2*d -1 digits long. Split the string representation of the square into two parts, l and r. The right hand part,r  must be d digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get ."""

#!/bin/python3

import math
import os
import random
import re
import sys

from MergeTwoSortedList import ListNode


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    res=[]
    for n in range(p,q+1):
        sq_n = n * n
        str_sq= str(sq_n)
        d=len(str(n))
        l=str_sq[:-d] if len(str_sq)>d else "0"
        r=str_sq[-d:]

        if int(l) + int(r) == n:
            res.append(n)
    if res:
        return " ".join(map(str,res))
    else:
        return "INVALID RANGE"

print(kaprekarNumbers(1,100))