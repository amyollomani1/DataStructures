from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Mine: idk if it works
#return kth smallest value (1-indexed( of all values of nodes in tree))
def KthSmallest(root, k):
    arr = []
    def dfs(root):
        if root:
            arr.append(root)
            dfs(root.left)
            dfs(root.right)
            
    dfs(root)
    sorted(arr)
    return arr[k-1]
    
#answer?
def kthSmallest(root, k):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stacl.append(curr)
            curr = curr.left
        curr = stack.pop()
        k-= 1
        if k == 0:
            return curr.val
        curr = curr.right
    