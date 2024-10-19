"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ## O((m+n)log(m+n)) time complexity and O(1) space compelxity
        # nums1[m:m+n]= nums2
        # nums1.sort()
        # print(nums1)

       ## Two pointer Method using python operators insert and pop: O((m+n)^2) time and o(1) space complexity
        # i,j=0,0
        # while j<n:
        #     if i!=0 and nums1[i]==0:
        #         nums1.insert(i,nums2[j])
        #         nums1.pop()
        #         i+=1
        #         j+=1
        #     elif nums1[i]<=nums2[j]:
        #         i+=1
        #     else:
        #         nums1.insert(i,nums2[j])
        #         nums1.pop()
        #         j+=1
        # return nums1

        ## Two pointer from end : O(m+n) time and O(1) space complexity
        i=m-1
        j=n-1
        k=m+n-1

        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1


sol=Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,5,6],3))