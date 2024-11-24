"""Given the root of a binary tree, invert the tree, and return its root."""
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        ##In place Recursive: Time: O(n), Space: O(h)
        # if root:
        #     root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        #     return root

        ## Using temp variable:Time: O(n), Space: O(h)
        # if not root:
        #     return
        #
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        #
        # tmp = left
        # root.left = right
        # root.right = tmp
        #
        # return root

        ##Iterative Approach: Time: O(n), Space: O(h)
        # if not root:
        #     return None
        # stack=[root]
        # while stack:
        #     node=stack.pop()
        #     node.left,node.right=node.right,node.left
        #
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return root

        ##Iterative Approach Using Queue: Time: O(n), Space: O(w)
        if not root:
            return None
        queue=deque([root])
        while queue:
            node=queue.popleft()
            node.left,node.right=node.right,node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


