"""Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    ##Time: O(n), Space: O(1)
    # w = list(w)
    # i = len(w) - 2
    # while i >= 0 and w[i] >= w[i + 1]:
    #     i -= 1
    # if i == -1:
    #     return "no answer"
    #
    # j = len(w) - 1
    # while w[j] <= w[i]:
    #     j -= 1
    # w[i], w[j] = w[j], w[i]
    # w = w[:i + 1] + w[i + 1:][::-1]
    # return "".join(w)

    ##Using For Loop: Time: O(n), Space: O(1)
    n=len(w)
    i=-1
    for x in range(n-2,-1,-1):
        if w[x]<w[x+1]:
            i=x
            break
    if i == -1:
        return "no answer"
    j = -1
    for y in range(n - 1, i, -1):
        if w[y] > w[i]:
            j = y
            break
    w = list(w)
    w[i], w[j] = w[j], w[i]
    w = w[:i + 1] + w[i + 1:][::-1]
    return "".join(w)

print(biggerIsGreater("abcde"))