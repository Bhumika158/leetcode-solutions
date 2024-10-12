"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""
from sys import prefix


class Solution(object):
    def longestCommonPrefix(self, strs):
        ## O(m*l*n) time and O(L) space complexity, where m=number of strings,
        #           l=length of first string and n=length of current string being checked.
        # first= strs[0]
        # for i in range(1,len(strs)):
        #     while not first in strs[i]:
        #         first=first[:-1]
        #
        # return first

        ## Horizontal Scanning : O(M*L) time and O(1) space complexity without considering input
        if not strs:
            return ""

        prefix=strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix

        ##Vertical Scanning: O(M*L) time and O(1) space complexity without considering input
        # if not strs:
        #     return ""
        #
        # for i in range(len(strs[0])):
        #     char = strs[0][i]
        #     for s in strs[1:]:
        #         if i >= len(s) or s[i] != char:
        #             return strs[0][:i]
        # return strs[0]

        ##Binary Search: O(m*L*log l) time and O(1) space complexity
        # if not strs:
        #     return ("")
        # min_length= min(len(s) for s in strs)
        # low,high=1,min_length
        #
        # def iscommonprefix(length):
        #     prefix= strs[0][:length]
        #     return all(s.startswith(prefix) for s in strs)
        #
        # while low<=high:
        #     mid= (low+high)//2
        #     if iscommonprefix(mid):
        #         low=mid+1
        #     else:
        #         high= mid-1
        # return strs[0][:(low+high)//2]

sol=Solution()
print("ans",sol.longestCommonPrefix(["flower","flow","flight","fly"]))