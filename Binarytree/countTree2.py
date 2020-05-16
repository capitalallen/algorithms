# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(l, r):
            if l > r:
                return None

            var = preorder.pop(0)
            root = TreeNode(var)
            index = d[var]
            root.left = helper(l, index-1)
            root.right = helper(index+1, r)

            return root

        d = {inorder[i]: i for i in range(len(inorder))}
        return helper(0, len(inorder)-1)
