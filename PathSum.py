"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        ##DFS: Time: O(n), Space: O(h)
        # def hasSum(root,cur_sum):
        #     if not root:
        #         return False
        #
        #     cur_sum+=root.val
        #     if not root.left and not root.right:
        #         return cur_sum==targetSum
        #
        #     return hasSum(root.left,cur_sum) or hasSum(root.right,cur_sum)
        #
        # return hasSum(root,0)

        ##In-Place recursive call: Time: O(n), Space: O(h):
        if root == None:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True

        remainingSum = targetSum - root.val

        return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)