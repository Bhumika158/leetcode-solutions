"""You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread. Your subjects are in a line, and some of them already have some loaves. Times are hard and your castle's food stocks are dwindling, so you must distribute as few loaves as possible according to the following rules:

Every time you give a loaf of bread to some person , you must also give a loaf of bread to the person immediately in front of or behind them in the line (i.e., persons i+1 or i-1).
After all the bread is distributed, each person must have an even number of loaves.
Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute to satisfy the two rules above. If this is not possible, print NO."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    l=len(B)
    loaf=0
    odd_count = sum(1 for x in B if x % 2 != 0)
    if odd_count%2!=0:
        return "NO"
    for i in range(l-1):
        if not B[i]%2==0:
            B[i]+=1
            B[i+1]+=1
            loaf+=2
    return str(loaf)

print(fairRations([2,3,4,5,6]))