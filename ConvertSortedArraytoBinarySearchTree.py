"""Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree."""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        ## Recursive Approach: Time:O(n) , Space: O(Log n)
        def helper(l,r):
            if l>r:
                return None
            m=(l+r)//2
            root= TreeNode(nums[m])
            root.left= helper(l,m-1)
            root.right= helper(m+1,r)
            return root
        return helper(0,len(nums)-1)

sol=Solution()
print(sol.sortedArrayToBST([-10,-3,0,5,9]))