"""Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days[i,...,j],  and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where |i-reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range."""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    ##Time: O(n⋅log j)) where n=j-i+1, Space: O(log(j))
    # beautifulDay=0
    # for i in range(i,j+1):
    #     if abs(i - int(str(i)[::-1])) %k==0:
    #         beautifulDay+=1
    # return beautifulDay

    ##Mathematical Conversion: O(n log j), Space: O(1)
    def reverseNum(n):
        rev=0
        while n>0:
            rev= rev*10+ n%10
            n//=10
        return rev

    beautifulDay = 0
    for day in range(i, j + 1):
        if abs(day - reverseNum(day)) % k == 0:
            beautifulDay += 1
    return beautifulDay



print(beautifulDays(20,23,6))