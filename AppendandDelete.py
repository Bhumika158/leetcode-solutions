"""You have two strings of lowercase English letters. You can perform two types of operations on the first string:

1) Append a lowercase English letter to the end of the string.
2) Delete the last character of the string. Performing this operation on an empty string results in an empty string.
Given an integer,k, and two strings,s  and t, determine whether or not you can convert  to  by performing exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    c=0
    for i in range(min(len(s),len(t))):
        if s[i]==t[i]:
            c+=1
        else:
            break
    total_operations= (len(s)-c)+ (len(t)-c)
    print(total_operations)
    if k>=total_operations and (k-total_operations)%2==0:
        return "Yes"
    elif k>=len(s)+len(t):
        return "Yes"
    else:
        return "No"

print(appendAndDelete("aba","aba",7))