"""The factorial of the integer n, written n!, is defined as:
n!= n* (n-1)* (n-2)...1
Calculate and print the factorial of a given integer."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    ## Time: O(n), Space: O(1)
    j=1
    for i in range(2,n+1):
        j*=i
    return j

    ##In-built function: Time: O(nlogn), Space: O(1)
    # return math.factorial(n)



print(extraLongFactorials(6))