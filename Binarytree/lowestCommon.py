# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def helper(node, p, q):
            if not node:
                return False
            left = helper(node.left, p, q)
            right = helper(node.right, p, q)

            mid = node == p or node == q
            if mid+left+right >= 2:
                self.ans = node
            return mid or left or right
        helper(root, p, q)

        return self.ans
