"""You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        ##Iterative Approach: Time: O(h), Space: O(1)
        # while root:
        #     if root.val==val:
        #         return root
        #     elif val<root.val:
        #         root=root.left
        #     else:
        #         root=root.right
        # return None

        ## Recursive Approach: Time:O(h), Space: O(h)
        # if not root or root.val==val:
        #     return root
        # if val<root.val:
        #     return self.searchBST(root.left,val)
        # else:
        #     return self.searchBST(root.right,val)

        ##Binary Search Emulation - Recursive Approach: Time:O(h), Space: O(h)
        def BinarySearch(node,low,high):
            if not node or low > high:
                return None
            if node.val == val:
                return node
            elif node.val<val:
                return BinarySearch(node.right, node.val + 1, high)
            else:
                return BinarySearch(node.left, low , node.val - 1)
        return BinarySearch(root, float('-inf'), float('inf'))
