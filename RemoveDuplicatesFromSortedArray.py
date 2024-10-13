"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k."""

class Solution(object):
    def removeDuplicates(self, nums):

        ## O(n) time and O(1) space complexity
        l=0
        for r in range(1,len(nums)):
            if  nums[r]!=nums[l]:
                l+=1
                nums[l]=nums[r]
        return l+1


sol=Solution()
print(sol.removeDuplicates([1,1,2,3,5]))