"""Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value."""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    my_dic={}
    for i in arr:
        my_dic[i]=my_dic.get(i,0)+1
    print(my_dic)
    max_freq = max(my_dic.values())
    l=len(arr)
    return l-max_freq

print(equalizeArray([1,2,3,1,2,3,3,3]))