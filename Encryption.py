"""An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:
floor(root(L))<=root<=column<=ceil(root(L))
"""
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    ##Time: O(n), Space: O(n)
    new_s=s.replace(" ","")
    l=len(new_s)
    row=math.floor(math.sqrt(l))
    column= math.ceil((math.sqrt(l)))
    if row * column < l:
        row += 1
    grid= [new_s[i:i+column] for i in range(0,l,column)]
    padded_rows = [row.ljust(column) for row in grid]
    result = ' '.join([''.join(col).strip() for col in zip(*padded_rows)])

    return result

print(encryption("feedthedog"))