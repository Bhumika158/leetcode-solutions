"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        ## Recursive Method: O(n) time and o(h) space complexity, where n is number of nodes in both trees and h is height of tree
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val!=q.val:
        #     return False
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        ## Iterative Approach: DFS using Stack: O(n) time and o(h) space complexity, where n is number of nodes in both trees and h is height of tree
        stack=[(p,q)]
        while stack:
            n1,n2=stack.pop()

            if not n1 and not n2:
                continue

            if not n1 or not n2 or n1.val!=n2.val:
                return False

            stack.append((n1.left,n2.left))
            stack.append((n1.right,n2.right))
        return True

