"""You are given a string,S, consisting of lowercase English letters.

A string is beautiful with respect to S if it can be derived from S by removing exactly 2 characters.

Find and print the number of different strings that are beautiful with respect to S."""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'beautifulStrings' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#

def beautifulStrings(s):
    n=len(s)
    res = set()
    for i in range(n):
        for j in range(i+1,n):
            new_hash = hash(s[:i] + s[i+1:j] + s[j+1:])
            res.add(new_hash)
    return len(res)


print(beautifulStrings("abba"))