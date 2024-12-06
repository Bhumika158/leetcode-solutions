"""Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Time: O(n), Space: O(1)
    count=0
    n=len(s)

    if m>n:
        return 0

    current_sum= sum(s[:m])
    if current_sum==d:
        count+=1

    for i in range(m,n):
        current_sum+= s[i]-s[i-m]
        if current_sum==d:
            count+=1

    return count
print(birthday([2,2,1,3,2],4,2))