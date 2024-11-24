"""Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ##DFS: Time: O(n), Space: O(m)
        largest_diameter=[0]
        def height(root):
            if root is None:
                return 0

            left_height= height(root.left)
            right_height=height(root.right)
            diameter= left_height+ right_height
            largest_diameter[0]= max(largest_diameter[0],diameter)

            return 1+ max(left_height,right_height)
        height(root)
        return largest_diameter[0]