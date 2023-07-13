class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#diamter is longest path between any two nodes
#starting from the bottom: visit each node at most 1 time
#TC = O(n)
#much better solution

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = [0]
    
    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], 2 + left + right)
        
        return 1 + max(left,right)
    dfs(root)
    return res[0]
    


#ChatGBT
#TC is O(n^2) since for each node, depth is calculated of its left and right subtrees resulting in O(n) operations
#worst case where tree is skewed, results in O(n^2) TC
#SC is O(n) due to recursive calls to stack
def diameterOfBinaryTree(root):
    def depth(node): #finds height
        if node is None: return 0
        return max(depth(node.left), depth(node.right)) + 1

    def diameter(node):
        if node is None:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        left_diameter = diameter(node.left)
        right_diameter = diameter(node.right)
        
        #this returns max length among all three cases
        return max(left_depth + right_depth, left_diameter, right_diameter)

    return diameter(root)