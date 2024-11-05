"""Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ## BFS Approach: O(n) , Space: O(n)
        # if not root:
        #     return 0
        # q=deque([root])
        # res=0
        #
        # while q:
        #     node=q.popleft()
        #
        #     if node.left:
        #         q.append(node.left)
        #         if not node.left.left and not node.left.right:
        #             res+= node.left.val
        #
        #     if node.right:
        #         q.append(node.right)
        # return res

        ## Recursive Approach:Time: O(n) , Space: O(H), O(n) for worst case, O(log n) for balanced tree
        # if not root:
        #     return 0
        # if root.left and not root.left.left and not root.left.right:
        #     return root.left.val + self.sumOfLeftLeaves(root.right)
        # return self.sumOfLeftLeaves(root.left)+ self.sumOfLeftLeaves(root.right)

        ## Iterative using Stack:Time: O(n) , Space: O(H), O(n) for worst case, O(log n) for balanced tree
        if not root:
            return 0
        stack=[root]
        res=0

        while stack:
            node=stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    res+= node.left.val
                else:
                    stack.append(node.left)

            if node.right:
                stack.append(node.right)
        return res
