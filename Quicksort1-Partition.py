"""The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm with a running time of O(N^2). In these next few challenges, we're covering a divide-and-conquer algorithm called Quicksort (also known as Partition Sort). This challenge is a modified version of the algorithm that only addresses partitioning. It is implemented as follows:

Step 1: Divide
Choose some pivot element,p , and partition your unsorted array,arr , into three smaller arrays: left,right and equal, where each element in left<p, each element in right>p, and each element in equal=p."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    p=arr[0]
    left=[]
    right=[]
    equal=[p]
    for i in range(1,len(arr)):
        if arr[i]>p:
            right.append(arr[i])
        elif arr[i]<p:
            left.append(arr[i])
        else:
            equal.append(arr[i])
    return left+equal+right

print(quickSort([4,5,3,4,7,2]))