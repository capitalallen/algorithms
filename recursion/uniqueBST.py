# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(start,end):
            if start>end:
                return [None,]
            allTree = []
            for i in range(start,end+1):
                leftTree = helper(start,i-1)
                rightTree =helper(i+1,end)
                
                for l in leftTree:
                    for r in rightTree:
                        currentTree = TreeNode(i)
                        currentTree.left = l
                        currentTree.right = r 
                        allTree.append(currentTree)
            return allTree
        return helper(1,n) if n else []