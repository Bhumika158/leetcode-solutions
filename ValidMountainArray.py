"""Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]"""

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ## Using max to identify the peak: Time: O(n) and Space: O(1)
        # maxindex= arr.index(max(arr))
        # if len(arr)<3 or maxindex==0 or maxindex==len(arr)-1:
        #     return False
        # for i in range(0,maxindex):
        #     if not arr[i]<arr[i+1]:
        #         return False
        #
        # for i in range(maxindex,len(arr)-1):
        #     if not arr[i]>arr[i+1]:
        #         return False
        #
        # return True

        ## Efficient Solution: Time:O(n), Space: O(1)
        n=len(arr)
        if n<3:
            return False
        l,r=0,n-1
        while l<n-1 and arr[l]< arr[l+1]:
            l+=1
        while r>0 and arr[r]<arr[r-1]:
            r-=1
        return l==r and l!=0 and r!=n-1



sol=Solution()
print(sol.validMountainArray([0,1,2,3,4,8,9,10,11,12,11]))