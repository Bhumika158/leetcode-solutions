"""Given a sequence x1,x2,x3...x26, construct a string,S , that meets the following conditions:

1) The frequency of letter 'a' in S is exactly x1, the frequency of letter 'b' in S is exactly x2, and so on.
2) Let's assume characters of S are numbered from 1 to N, where sum (Xi) from 0 to n is equal to N. We apply the KMP algorithm to S and get a table, kmp, of size N. You must ensure that the sum of kmp[i] for all i is minimal.
If there are multiple strings which fulfill the above conditions, print the lexicographically smallest one."""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kmp' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY x as parameter.
#

def kmp(x):
    # Step 1: Create a list of characters with their frequencies
    char_freq = [(chr(ord('a') + i), x[i]) for i in range(26) if x[i] > 0]
    # Step 2: Sort characters lexicographically
    char_freq.sort()

    result = []
    prev_char = None

    while char_freq:
        # Sort dynamically by frequency (descending) and lexicographical order
        char_freq.sort(key=lambda cf: (-cf[1], cf[0]))

        for idx in range(len(char_freq)):
            char, freq = char_freq[idx]
            if prev_char != char:  # Avoid repeating the same character
                result.append(char)
                prev_char = char
                char_freq[idx] = (char, freq - 1)
                if char_freq[idx][1] == 0:  # Remove the character if its frequency is 0
                    char_freq.pop(idx)
                break

    return ''.join(result)


# Test cases
print(kmp([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0]))  # Should output "mmsmsssswwwww"
print(kmp([2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Should output "aabb"
print(kmp([3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]))  # Should output "zaaaz"
