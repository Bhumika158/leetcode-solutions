"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ##Recursive Approach:O(n) time and O(h) space complexity
        # def dfs(left,right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
        #
        #     return (left.val== right.val and dfs(left.left,right.right) and dfs(left.right,right.left))
        #
        # return dfs(root.left,root.right)

        ## Iterative Approach: DFS using Stack: O(n) time and o(h) space complexity, where n is number of nodes in both trees and h is height of tree
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()

            if not left and not right:
                continue

            if not left or not right or left.val != right.val:
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
