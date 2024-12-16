"""An integer d is a divisor of an integer n if the remainder of n/d=0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    ##Arithmetic Operation: Time: O(log(n)), Space: O(1)
    # c=0
    # a=n
    # while a!=0:
    #     if a%10!=0 and n%(a%10)==0:
    #         c+=1
    #     a=a//10
    # return c

    ##String Operation: Time: O(log(n)), Space: O(1)
    c=0
    for digits in str(n):
        d=int(digits)
        if d!=0 and n%d==0:
            c+=1
    return c

print(findDigits(1012))