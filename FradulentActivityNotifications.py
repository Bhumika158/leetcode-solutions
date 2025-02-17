"""HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2* the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over all n days."""

#!/bin/python3

import math
import os
import random
import re
import sys

from numpy.ma.extras import median


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    ## Time: O(n*d log d), Space: O(d)
    # notify = 0
    # for i in range(d,len(expenditure)):
    #     last_days_expend = sorted(expenditure[i-d:i])
    #     current_day_expend= expenditure[i]
    #     e_o = len(last_days_expend)
    #     print(last_days_expend,current_day_expend,e_o)
    #     if e_o%2 ==0:
    #         median_val=(last_days_expend[e_o//2] + last_days_expend[(e_o//2)-1])/2
    #         if current_day_expend >= 2* median_val:
    #             notify+=1
    #     else:
    #         median_val = last_days_expend[e_o//2]
    #         if current_day_expend >= 2* median_val:
    #             notify+=1
    # return notify

    ##Using CountingSort : Time: O(n), Space: O(1)
    notify =0
    count = [0] *201 #constrain says n range upto 200
    for i in range(d):
        count[expenditure[i]]+=1
    for i in range(d,len(expenditure)):
        median_val = get_median(count,d)
        if expenditure[i] >= 2*median_val:
            notify+=1
        count[expenditure[i]] +=1
        count[expenditure[i-d]] -=1
    return notify


def get_median(count,d):
    median_pos= d//2
    cumulative_count =0
    median1,median2= None,None
    for i in range(len(count)):
        cumulative_count += count[i]
        if median1 is None and cumulative_count> median_pos:
            median1 =i
        if median2 is None and cumulative_count > median_pos-1:
            median2 = i
        if median1 is not None and median2 is not None:
            break
    return (median1 +median2)/2 if d%2==0 else median1



print(activityNotifications([1,2,3,4,4],4))
