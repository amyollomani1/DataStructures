class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#start at root, since we know root is ansector of all nodes
#O(logn) since you only visit 1 node per level, so its propotional to height, which is usually logn
def LCA(self,root, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    cur = root
    while cur:
        #if p and q are > than root, then move to the right
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        #if p and q are < root, then move to left
        elif p.val < cur.val and q.cal < cur.val:
            cur = cur.left
        else: #Then cur is LCA
            return cur

#Another solution, faster for some reason
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
    
        # If both p and q are smaller than root, LCA must be in the left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both p and q are greater than root, LCA must be in the right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If none of the above conditions are met, root is the LCA
        return root