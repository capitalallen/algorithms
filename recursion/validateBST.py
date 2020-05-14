# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        return self.helper(root,float('-inf'),float('inf'))
    def helper(self,node,l,h):
        if not node:
            return True
        
        val = node.val
        if val<=l or val>= h:
            return False
        
        if not self.helper(node.right,val,h):
            return False 
        if not self.helper(node.left,l,val):
            return False 
        return True 
    