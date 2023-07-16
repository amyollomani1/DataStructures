class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def dfs(p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return False
    return dfs(p, q)