"""An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ##Binary Search: Time: O(nlogn + mlogm), Space: O(m)
    unique_ranks=sorted(set(ranked), reverse=True)
    result=[]

    def binary_search(arr,target):
        l,r=0,len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                r=mid-1
            else:
                l = mid + 1
        return l

    for score in player:
        position= binary_search(unique_ranks,score)
        result.append(position+1)
    return result

    ##Iteration: Time: O(m+n), Space: O(1)
    # unique_ranked = sorted(set(ranked), reverse=True)
    # result = []
    # index = len(unique_ranked) - 1
    # for score in player:
    #     print(index,score,unique_ranked)
    #     while index >= 0 and score >= unique_ranked[index]:
    #         index -= 1
    #     result.append(index + 2)
    # return result

print(climbingLeaderboard([100,90,90,80],[70,80,105]))