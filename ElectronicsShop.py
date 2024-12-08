"""A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return ."""

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    ## Time: O(n*m), Space: O(k)
    # options = []
    # for i in keyboards:
    #     for j in drives:
    #         if i+j<=b:
    #             options.append(i + j)
    # print(options)
    # if not options:
    #     return -1
    # else:
    #     return max(options)

    ## Time: O(n*m), Space: O(1)
    # max_cost = -1
    # for keyboard in keyboards:
    #     for drive in drives:
    #         cost = keyboard + drive
    #         if cost <= b:
    #             max_cost = max(max_cost, cost)
    #
    # return max_cost

    ##Sorting: Time: O(nlogn + mlogm), Space: O(1)
    keyboards = sorted(keyboards)
    drives = sorted(drives, reverse=True)
    max_cost = -1
    i, j = 0, 0
    print(keyboards,drives)
    while i < len(keyboards) and j < len(drives):
        cost = keyboards[i] + drives[j]

        if cost>b:
            j+=1
        else:
            max_cost=max(max_cost,cost)
            i+=1
    return max_cost

print(getMoneySpent([3, 1],[5, 2, 8],10))