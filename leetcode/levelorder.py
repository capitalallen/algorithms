def levelOrder(self, root):
    # write your code here
    if not root: 
        return []
    queue, res = [root,], []
    
    while queue:
        cur_level, size = [], len(queue)
        for i in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            cur_level.append(node.val)
        res.append(cur_level)
    return res 