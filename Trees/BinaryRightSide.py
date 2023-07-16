from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#my guess
def rightside(root):
    res = []
    if root:
        res.append(root.val)
    while root.right:
        root = root.right
        res.append(root.val)
    
    return res
    
    
#answer:
def rightside(root):
    res = []
    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
        if node:
            res.append(node.val)
            
    return res
   