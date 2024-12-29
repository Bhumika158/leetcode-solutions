"""Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to its nearest space station."""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    ##Time: O(n*m), Space: O(1)
    # min_dis=float("inf")
    # res=[]
    # for i in range(n):
    #     for j in c:
    #         min_dis = min(min_dis, abs(i - j))
    #     res.append(min_dis)
    #     min_dis = float("inf")
    # return max(res)

    ##Sorting: Time: O(mlogm), Space: O(1)
    c.sort()
    max_distance = 0
    max_distance = max(max_distance, c[0])
    max_distance = max(max_distance, n - 1 - c[-1])

    for i in range(1, len(c)):
        max_distance = max(max_distance, (c[i] - c[i - 1]) // 2)

    return max_distance
print(flatlandSpaceStations(6,[0,1,2,3,4,5]))