"""Neo has a complex matrix script. The matrix script is a N X M grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space ' ' for better readability."""

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])


matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded= ""
for i in range(m):
    for j in range(n):
        decoded+=matrix[j][i]

print(decoded)
pattern = r'(?<=[a-zA-Z])[^\w]+(?=[\w])'
res= re.sub(pattern,' ',decoded)
