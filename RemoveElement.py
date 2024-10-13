"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k."""

class Solution(object):
    def removeElement(self, nums, val):
        ## Swap and Remove (for unordered array): O(n) time and O(1) space complexity
        # l,r=0,len(nums)
        # while l<r:
        #     if nums[l]==val:
        #         nums[l],nums[r-1]=nums[r-1],nums[l]
        #         r-=1
        #     else:
        #         l+=1
        # return r

        ## two pointer method: O(n) time and o(1) space complexity
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


sol=Solution()
print(sol.removeElement([1],1))