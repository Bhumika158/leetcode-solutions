"""Andy wants to play a game with his little brother, Bob. The game starts with an array of distinct integers and the rules are as follows:

Bob always plays first.
In a single move, a player chooses the maximum element in the array. He removes it and all elements to its right.
The last player who can make a move wins.
Andy and Bob play g games. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print ANDY; if Bob wins, print BOB.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    ##Time: O(n^2), Space: O(n)
    # count=0
    # while len(arr)>0:
    #     arr=arr[:arr.index(max(arr))]
    #     count+=1
    #
    # if (count-1)%2==0:
    #     return "BOB"
    # else:
    #     return "ANDY"

    ##Time: O(n), Space: O(1)
    max_so_far = float('-inf')
    count = 0

    for num in arr:
        if num > max_so_far:
            max_so_far = num
            count += 1


    return "BOB" if count % 2 == 1 else "ANDY"

print(gamingArray([3,1]))