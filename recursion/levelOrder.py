# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root,]
        levels = []
        if not root:
            return levels 
        while queue:
            num = len(queue)
            arr = []
            for _ in range(num):
                curr = queue.pop(0)
                
                arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levels.append(arr)
        return levels 
    