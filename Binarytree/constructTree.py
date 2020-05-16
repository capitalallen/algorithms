# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def helper(l, r):
            if l > r:
                return None
            var = postorder.pop()
            root = TreeNode(var)
            index = d[var]
            root.right = helper(index+1, r)
            root.left = helper(l, index-1)
            return root
        d = {inorder[i]: i for i in range(len(inorder))}
        return helper(0, len(inorder)-1)
