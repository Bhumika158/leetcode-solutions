"""Given an array of integers and a positive integer , determine the number of  pairs where  and  +  is divisible by ."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Brute Force: Time: O(n^2), Space: O(1)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j]) % k==0:
                count+=1
    return count



print(divisibleSumPairs(6,5,[1,2,3,4,5,6]))