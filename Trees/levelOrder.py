from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#ChatGPT
def levelOrder(root):
    if not root:
        return []
    
    result = [] #stores levels of tree
    queue = deque([root]) #intilizes queue and appends root simultaniously
    
    while queue:
        level = [] # stores values at current level
        level_size = len(queue) #keeps track of nodes at curr level
        
        for _ in range(level_size):
            node = queue.popleft() #remove node at front of queue
            level.append(node.val) #add value to level
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

#leetcode,
def levelOrder(root):
    res = []
    q = deque()
    if root:
        q.append(root)

    while q:
        val = []
        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(val)
    return res