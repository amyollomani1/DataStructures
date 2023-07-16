class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def sameTree(root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val: #make sure they are both not empty and are same val
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        return False

    if not subRoot:
        return True #note: a null subtree is a subtree of another tree
    if not root:
        return False #if root is null but subtree isn't null, then it isn't subtree
    if sameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #check is its a subtree of the left tree of s

#TC is O(S * T)
