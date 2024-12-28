"""You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    ##Time: O(n^2), Space: O(n)
    # res = []
    # while arr!=[0]*len(arr):
    #     length_of_cut= min(x for x in arr if x > 0)
    #     sticks_cut=0
    #     for i in range(len(arr)):
    #         if arr[i]!=0:
    #             arr[i]-=length_of_cut
    #             sticks_cut+=1
    #     res.append(sticks_cut)
    # return res

    ##Using Sorting, Time: O(n log n), Space: O(n)
    arr.sort()
    res=[]
    n=len(arr)
    for i in range(n):
        if i==0 or arr[i]!=arr[i-1]:
            res.append(n-i)
    return res



print(cutTheSticks([5,4,4,2,2,8]))