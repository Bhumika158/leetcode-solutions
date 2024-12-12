"""Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to ."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    ##Time: O(n log n), Space: O(1)
    a.sort()
    l,max_len=0,0

    for r in range(len(a)):
        while a[r]-a[l]>1:
            l+=1
        max_len=max(max_len,r-l+1)
    return max_len


print(pickingNumbers([1,1,2,2,4,4,5,5,5]))