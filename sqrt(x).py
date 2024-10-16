"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""

class Solution(object):
    def mySqrt(self, x):
        ## Binary search: O(log(x)) time and O(1) space complexity
        # l,r=0,x
        # while l<=r:
        #     mid=(l+r)//2
        #     if mid*mid==x:
        #         return mid
        #     elif mid*mid <x:
        #         l=mid+1
        #     else:
        #         r=mid-1
        # return r

        ## Newton's method: O(log(x)) time and O(1) space complexity
        if x == 0:
            return 0
        approx = x
        while True:
            better_approx = (approx + x // approx) // 2
            if better_approx >= approx:
                break
            approx = better_approx
        return approx



sol=Solution()
print(sol.mySqrt(16))