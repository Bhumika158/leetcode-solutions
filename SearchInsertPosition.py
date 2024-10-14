"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""
class Solution(object):
    def searchInsert(self, nums, target):
        ## O(n.m) time complexity and O(1) space complexity:
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     for i in range(len(nums)):
        #         if nums[i]>target:
        #             return i

        ## O(log n) time and O(1) space complexity:
        l,r=0,len(nums)-1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return l

sol=Solution()
print(sol.searchInsert([1,3,5,6],8))