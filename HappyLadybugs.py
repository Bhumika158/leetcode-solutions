"""Happy Ladybugs is a board game having the following properties:

The board is represented by a string,b, of length n. The ith character of the string,b[i], denotes the ith cell of the board.
If b[i] is an underscore (i.e., _), it means the ith cell of the board is empty.
If  b[i] is an uppercase English alphabetic letter (ascii[A-Z]), it means the ith cell contains a ladybug of color b[i].
String b will not contain any other characters.
A ladybug is happy only when its left or right adjacent cell (i.e.,b[i+-1]) is occupied by another ladybug having the same color.
In a single move, you can move a ladybug from its current position to any empty cell.
Given the values of n and b for g games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, return YES if all the ladybugs can be made happy through some number of moves. Otherwise, return NO."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    my_dic={}
    for i in b:
        if i not in my_dic:
            my_dic[i]=1
        else:
            my_dic[i]+=1
    for i,val in my_dic.items():
        if i!="_" and val==1:
            return "NO"
    if "_" not in b:
        for i in range(1,len(b)):
            print(i,b[i],b[i-1])
            if b[i]!=b[i-1] and b[i]!=b[i+1]:
                return "NO"
    return "YES"



print(happyLadybugs("AABBCCDD"))