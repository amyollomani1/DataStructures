from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#node is good if all its parents nodes are smaller than it
#return number of good nodes in it
def goodNodes(root):
    
    def dfs(node, maxVal):
        if not node:
            return None
        res = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        res += dfs(node.left, maxVal)
        res += dfs(node.right, maxVal)
        return res
        
    return dfs(root, root.val)