"""Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums."""

class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## O(n) time and O(1) space complexity
        n=len(nums)
        min_val= min(nums)
        max_val=max(nums)
        if min_val==max_val:
            return 0
        else:
            return n-nums.count(min_val)-nums.count(max_val)

        ## Alternate Approach: without using min,max,count: O(n) time and O(1) space complexity:
        # min_val, max_val = float('inf'), float('-inf')
        # min_count, max_count = 0, 0
        #
        # for num in nums:
        #     if num < min_val:
        #         min_val = num
        #         min_count = 1
        #     elif num == min_val:
        #         min_count += 1
        #
        #     if num > max_val:
        #         max_val = num
        #         max_count = 1
        #     elif num == max_val:
        #         max_count += 1
        #
        # # The result is the total number of elements minus the min and max occurrences
        # n = len(nums)
        # if min_val == max_val:
        #     return 0
        # return n - min_count - max_count

        ## List Comprehension: O(n) time and O(1) space complexity:
        # min_val = min(nums)
        # max_val = max(nums)
        #
        # # Count elements that are strictly greater than min_num and strictly less than max_num
        # count = sum(1 for num in nums if min_val < num < max_val)
        #
        # return count

sol=Solution()
print(sol.countElements([0]))