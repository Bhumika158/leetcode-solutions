"""Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift."""


class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        ## O(n) time and space complexity
        if len(s)!=len(goal):
            return False
        s+=s
        if goal in s:
            return True
        else:
            return False

        #Above code can be reduced to: "return len(s)==len(goal) and goal in s+s"

sol=Solution()
print(sol.rotateString("abcde","abced"))