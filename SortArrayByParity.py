"""Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition."""

class Solution(object):
    def sortArrayByParity(self, nums):

        ## O(n) time and O(1) space complexity
        # k=len(nums)-1
        # output= [0] *len(nums)
        #
        # for i in range(len(nums)):
        #     if nums[i]%2!=0:
        #         output[k] = nums[i]
        #         k -= 1
        #     else:
        #         output[k]=nums[i]
        #         k-=1
        #
        # return output

        ##O(n) time and O(1) space complexity:
        l,r=0,len(nums)-1

        while l<r:
            while l<r and nums[l]%2==0:
                l+=1
            while l<r and nums[r]%2!=0:
                r-=1
            if l<r:
                nums[l],nums[r]=nums[r],nums[l]
        return nums

        ## Another Approach: O(n) time and O(1) space complexity
        # left = 0
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         nums[left],nums[i] = nums[i],nums[left]
        #         left += 1
        # return nums


sol=Solution()
print(sol.sortArrayByParity([3,1,2,5]))