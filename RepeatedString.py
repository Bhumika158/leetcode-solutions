"""There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer,n , find and print the number of letter a's in the first n letters of the infinite string."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    ##Time: O(l), Space: O(l)
    l=len(s)
    c_a= s.count("a")
    remain_c_a = sum(1 for i in range(n % l) if s[i] == 'a')
    return ((n//l)* c_a)+ remain_c_a

print(repeatedString("a",1000000000000))