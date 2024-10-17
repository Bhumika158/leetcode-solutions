"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""

class Solution(object):
    def climbStairs(self, n):
        ## O(n) time and O(1) space complexity
        one,two=1,1
        for i in range(n-1):
            temp=one
            one=one+ two
            two=temp
        return one

        ## DP : O(N) time and space complexity

        # ways = {}
        # ways[1] = 1
        # ways[2] = 2
        # if n <= 2:
        #     return ways[n]
        # for i in range(3, n + 1):
        #     ways[i] = ways[i - 1] + ways[i - 2]
        # return ways[n]


sol=Solution()
print(sol.climbStairs(3))