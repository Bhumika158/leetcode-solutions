"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## O(n^2) time complexity: Using two for Loops
        # for i in range(0,len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i]+ nums[j]==target:
        #             return [i,j]

        ## O(n log n) time complexity: Using Two pointer Method(works for sorted array).
        # nums_with_index = sorted(enumerate(nums), key=lambda x: x[1])
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     current_sum = nums_with_index[l][1] + nums_with_index[r][1]
        #     if current_sum == target:
        #         return [nums_with_index[l][0], nums_with_index[r][0]]
        #     elif current_sum < target:
        #         l += 1
        #     else:
        #         r -= 1

        ## O(n) time complexity: Using a dict(best for unsorted array).
        my_dic={}
        for i,num in enumerate(nums):
            if not target-num in my_dic:
                my_dic[num]=i
            else:
                return [i,my_dic[target-num]]


sol=Solution()
print(sol.twoSum([3,2,4],6))