"""Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: . Anna declines to eat item  which costs . If Brian calculates the bill correctly, Anna will pay . If he includes the cost of , he will calculate . In the second case, he should refund  to Anna."""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    actual= (sum(bill)-bill[k])//2
    if actual==b:
        print("Bon Appetit")
    else:
        print(b-actual)



print(bonAppetit([72,53,60,66,90,62,12,31,36,94],6,288))