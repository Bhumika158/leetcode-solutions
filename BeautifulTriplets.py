"""Given a sequence of integers a, a triplet (a[i),s[j],a[k]) is beautiful if:
i<j<k
a[j]-a[i]=a[k]-a[j]=d
Given an increasing sequenc of integers and the value of d, count the number of beautiful triplets in the sequence."""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    ##Time: O(n), Space: O(n)
    b_t=0
    arr_set=set(arr)
    for i in arr:
        if i+d in arr_set and i+(2*d) in arr_set:
            b_t+=1
    return b_t

print(beautifulTriplets(1,[2,2,3,4,5]))