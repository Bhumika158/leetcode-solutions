"""You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums."""

class Solution(object):
    def countHillValley(self, nums):
        ## Time: O(n) , Space: O(1)
        # n = len(nums)
        # sum = 0
        # for r in range(1, n - 1):
        #     if nums[r] == nums[r - 1]:
        #         continue
        #
        #     l = r + 1
        #     while l < n and nums[l] == nums[r]:
        #         l += 1
        #
        #     if l < n:
        #         if (nums[r] > nums[r - 1] and nums[r] > nums[l]) or (nums[r] < nums[r - 1] and nums[r] < nums[l]):
        #             sum += 1
        #     r = l - 1
        #
        # return sum

        ## Filtering Solution: Time: O(n), Space: O(n)
        # unique_nums = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         unique_nums.append(nums[i])
        #
        # sum = 0
        # for i in range(1, len(unique_nums) - 1):
        #     if (unique_nums[i] > unique_nums[i - 1] and unique_nums[i] > unique_nums[i + 1]) or \
        #             (unique_nums[i] < unique_nums[i - 1] and unique_nums[i] < unique_nums[i + 1]):
        #         sum += 1
        #
        # return sum

        ## Efficient and Concise Solution: Time: O(n) , Space O(1):
        sum, left = 0, nums[0]

        for i in range(1, len(nums) - 1):
            if (left < nums[i] and nums[i] > nums[i + 1]) or (left > nums[i] and nums[i] < nums[i + 1]):
                sum += 1
                left = nums[i]
        return sum



sol=Solution()
print("ans",sol.countHillValley([8,2,5,7,7,2,10,3,6,2]))