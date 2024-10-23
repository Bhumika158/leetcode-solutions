"""Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive)."""

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## O(n) time and space complexity
        ans=[]
        for i in nums:
            ans.append(nums[i])
        return ans


sol=Solution()
print(sol.buildArray([0,2,1,5,3,4]))