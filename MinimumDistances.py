"""The distance between two array values is the number of indices between them. Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, return -1."""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    ##Approach 1: Time: O(n^2), Space: O(n)
    # my_dic={}
    # for i,n in enumerate(a):
    #     if n not in my_dic:
    #         my_dic[n]=[]
    #     my_dic[n].append(i)
    # res=float("inf")
    # for ind in my_dic.values():
    #     if len(ind)>1:
    #         for i in range(len(ind)-1):
    #             for j in range(i+1,len(ind)):
    #                 res=min(res,abs(ind[i]-ind[j]))
    # return res

    ##Approach 2: Time: O(n), Space: O(n)
    my_dic={}
    min_dis= float("inf")
    for i, num in enumerate(a):
        if num in my_dic:
            min_dis=min(min_dis,i-my_dic[num])
        my_dic[num]=i
    return min_dis if min_dis != float("inf") else -1

print(minimumDistances([3,2,1,2,3,3]))