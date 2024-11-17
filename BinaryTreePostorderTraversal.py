"""Given the root of a binary tree, return the postorder traversal of its nodes' values."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ##Recursive Approach 1: Time: O(n), Space: O(n)
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        ## Recusrive Approach 2: Time: O(n), Space: O(n)
        # res=[]
        # def postorder(root):
        #     if not root:
        #         return []
        #     postorder(root.left)
        #     postorder(root.right)
        #     res.append(root.val)
        # postorder(root)
        # return res

        ##Iterative Approach: Time: O(n), Space: O(n)
        if not root:
            return []

        res = []
        stack1 = [root]
        stack2 = []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)

            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)

        while stack2:
            res.append(stack2.pop().val)

        return res