"""Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    ##Time: O(sqrt(b)-sqrt(a)), Space: O(1)
    # base= int(math.sqrt(a))
    # c=0
    # if base*base<a:
    #     base+=1
    # while a<=base*base <=b:
    #     c+=1
    #     base+=1
    # return c

    ##Time: O(1), Space: O(1)
    # x = math.ceil(math.sqrt(a))
    # y = math.floor(math.sqrt(b))
    # return max(0,y-x+1)

    ##Linear Approach: O(sqrt b), Space: O(1)
    # start = 1
    # while start * start < a:
    #     start += 1
    # count = 0
    # while start * start <= b:
    #     count += 1
    #     start += 1
    #
    # return count

    ##Binary Search : O(log b), Space: O(1)
    def find_start(a):
        l,r=1,a
        while l<=r:
            mid=(l+r)//2
            if mid*mid>=a:
                r=mid-1
            else:
                l=mid+1
        return l
    def find_end(b):
        l,r=1,b
        while l<=r:
            mid=(l+r)//2
            if mid*mid<=b:
                l=mid+1
            else:
                r=mid-1
        return r

    start= find_start(a)
    end= find_end(b)
    return max(0,end-start+1)

print(squares(3,9))