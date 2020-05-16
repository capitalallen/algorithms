"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:

        def helper(node, curr):
            if not node:
                return False
            if not node.left and not node.right and node.val == curr:
                return True
            curr -= node.val
            return helper(node.left, curr) or helper(node.right, curr)
        return helper(root, target)
