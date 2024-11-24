"""You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees."""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        ##Recursive Approach: Time: O(n), Space: O(h)
        # if not root1 and not root2:
        #     return None
        # v1= root1.val if root1 else 0
        # v2 = root2.val if root2 else 0
        #
        # root=TreeNode(v1+v2)
        #
        # root.left=self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        # root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        #
        # return root

        ##Recursive Approach with fewer lines: Time: O(n), Space: O(h)
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # root=TreeNode(root1.val+root2.val)
        # root.left=self.mergeTrees(root1.left,root2.left)
        # root.right= self.mergeTrees(root1.right,root2.right)
        #
        # return root

        ##Iterative Approach Using Stack: Time: O(n), Space: O(n)
        if not root1:
            return root2
        if not root2:
            return root1

        stack=[(root1,root2)]
        while stack:
             node1,node2= stack.pop()
             if not node1 or not node2:
                 continue
             node1.val+=node2.val

             if not node1.left:
                 node1.left=node2.left
             else:
                 stack.append((node1.left,node2.left))
             if not node1.right:
                 node1.right = node2.right
             else:
                 stack.append((node1.right, node2.right))
        return root1