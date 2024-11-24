"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)."""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ## BFS: Time: O(n), Space: O(m), n=no. of nodes, m=max no. of nodes at each level
        if not root:
            return []

        queue=deque([root])
        res=[]

        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

# Helper function to build a binary tree
def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


if __name__ == "__main__":
    tree_values = [3, 9, 20, None, None, 15, 7]
    root = build_tree(tree_values)

    solution = Solution()
    result = solution.levelOrder(root)

    # Print the result
    print("Level-order traversal using stack:", result)