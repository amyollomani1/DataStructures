from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Mine: idk if it works
def isBST(root):
    def dfs(root):
        if root is None:
            return True
        bool = False
        while root:
            if root.left:
                val = root.val
                root = root.left
                if val < root.val:
                    bool = False
                bool =  True
                bool = dfs(root.left)
            if root.right:
                val = root.val
                root = root.right
                if val > root.val:
                    bool =  False
                bool =  True
                bool =  dfs(root.right)
                
        return bool
    return dfs(root)
 
    
#Leetcode
def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True
        if not(left < node.val < right):
            return False
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    return valid(root, float("-inf", float("-inf")))

