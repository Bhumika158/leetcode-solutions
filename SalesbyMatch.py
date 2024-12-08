"""There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are."""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ##Time: O(n+k), Space: O(k)
    # my_dic={}
    # for i in ar:
    #     if i in my_dic:
    #         my_dic[i]+=1
    #     else:
    #         my_dic[i]=1
    # pairs=0
    # for i,freq in my_dic.items():
    #     pairs+=freq//2
    # return pairs

    ##Time: O(n), Space: O(n)
    unmatched = set()
    pairs = 0
    for i in ar:
        if i in unmatched:
            unmatched.remove(i)
            pairs+=1
        else:
            unmatched.add(i)
    return pairs

print(sockMerchant(7,[1,2,1,2,1,3,2]))