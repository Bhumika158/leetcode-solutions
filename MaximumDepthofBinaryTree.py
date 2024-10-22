"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        ## Recursive Approach:O(n) time and space complexity. Best space complexity is O(log n)
        # if not root:
        #     return 0
        # return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))

        ##Iteratibve approach: BFS O(n) time and space complexity . Best space complexity is O(n)
        # if not root:
        #     return 0
        # level=1
        # q=deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node=q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level+=1
        # return level

        ##Iterative Approach: DFS: O(n) time and space complexity. Best space complexity is O(log n)
        stack=[[root,1]]
        res=0
        while stack:
            node,depth=stack.pop()
            if node:
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right, depth + 1])
        return res