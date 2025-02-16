"""The median of a list of numbers is essentially its middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, find the median?"""

#!/bin/python3

import math
import os
import random
import re
import sys

from FindDigits import findDigits


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    ## CountingSort: Time: O(n+k), Spacee: O(k)
    min_val, max_val= min(arr),max(arr)
    range_size = max_val - min_val + 1
    res=[0]*range_size
    for i in arr:
        res[i-min_val]+=1
    median_pos= len(arr)//2
    count= 0
    for index,n in enumerate(res):
        count+=n
        if count > median_pos:
            return index+min_val


print(findMedian([5,3,1,2,4]))