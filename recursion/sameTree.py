# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def check(p,q):
            if not p and not q:
                return True 
            if not p or not q:
                return False 
            if p.val != q.val:
                return False 
            return True 
        queue = [(p,q),]
        while queue:
            p,q = queue.pop(0)
            if not check(p,q):
                return False 
                # print(p.val,q.val)
            if p and q:
                queue.append((p.left,q.left))
                queue.append((p.right,q.right))
        return True 
    