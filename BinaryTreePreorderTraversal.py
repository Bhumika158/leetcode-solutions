"""Given the root of a binary tree, return the preorder traversal of its nodes' values."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ##Recursive Approach 1: Time: O(n), Space:O(n)
        # if not root:
        #     return []

        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        ## Recursive Approach 2: Time: O(n), Space:O(n)
        # res=[]
        # def preorder(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)

        # preorder(root)
        # return res

        ##Iterative Approach: Time: O(n), Space:O(n)
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
