"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ## Recursive Approach: Time: O(n), Space: O(h)
        # if not root or root == p or root == q:
        #     return root
        #
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        #
        # if left and right:
        #     return root
        #
        # return left if left else right

        ##Iterative Approach : Time: O(n), Space: O(n)
        # parent= {root:None}
        #
        # stack=[root]
        #
        # while p not in parent or q not in parent:
        #     node=stack.pop()
        #
        #     if node.left:
        #         parent[node.left]=node
        #         stack.append(node.left)
        #     if node.right:
        #         parent[node.right]=node
        #         stack.append(node.right)
        # ancestor=set()
        # while p:
        #     ancestor.add(p)
        #     p=parent[p]
        # while q not in ancestor:
        #     q=parent[q]
        #
        # return q

        ##Recursive Approach using helper func: Time: O(h), Space: O(h)
        def search(node):
            if not node or node==p or node==q:
                return node
            if node.val>p.val or node.val>q.val:
                return search(node.left)
            if node.val<p.val or node.val<q.val:
                return search(node.right)

            return node
        return search(root)


