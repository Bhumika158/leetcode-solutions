"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ##Divide-and-Conquer (Range Validation): Time: O(n), Space:O(h)
        # def valid(node,left,right):
        #     if not node:
        #         return True
        #     if not (node.val>left and node.val<right):
        #         return False
        #     return (valid(node.left,left,node.val) and valid(node.right,node.val,right))
        #
        # return valid(root,float("-inf"),float("inf"))

        ##Recursive In-Order Traversal: Validating current Node is more than prev node as Inorder generates sorted sequence.: Time: O(n), Space:O(h)
        # def inOrder(node,prev):
        #     if not node:
        #         return True
        #     if not inOrder(node.left,prev):
        #         return False
        #     if prev[0] is not None and node.val<=prev[0]:
        #         return False
        #     prev[0]=node.val
        #
        #     return inOrder(node.right,prev)
        # return inOrder(root,[None])

        ##Iterative In-Order Traversal: Time: O(n), Space:O(h)
        stack=[]
        prev=None
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if prev is not None and root.val<=prev:
                return False
            prev=root.val

            root=root.right
        return True