"""The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement."""

class Solution(object):
    def bitwiseComplement(self, n):

        ## O(log n) time and space complexity
        # bin_n=bin(n)[2:]
        # d = {'0': '1', '1': '0'}
        # reversed_n=''.join(d[x] for x in bin_n)
        # return int(reversed_n,2)

        ## XOR Approach: O(log n) time and O(1) space complexity:
        if n==0:
            return 1

        mask = (1 << n.bit_length()) - 1
        return n ^ mask


sol=Solution()
print(sol.bitwiseComplement(5))