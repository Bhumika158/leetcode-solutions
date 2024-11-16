"""Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k."""


class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ## Brute-Force Solution: Time: O(n^2), Space: O(1)
        count=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (i*j)%k==0 and nums[i]==nums[j]:
                    count+=1
        return count


sol=Solution()
print(sol.countPairs([3,1,2,2,2,1,3],2))