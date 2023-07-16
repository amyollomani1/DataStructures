
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Me
# O(n^2) checks if whole tree is from the root down
# height function itself is O(n), called recursivly n times so its O(n^2)
def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right))+1
        def checkBal(root):
            if not root:
                return True

            leftH = height(root.left)
            rightH = height(root.right)
            
            if abs(rightH - leftH) >1:
                return False
        
            return checkBal(root.left) and checkBal(root.right)
        return checkBal(root)
    
#Chat gbt optimized
def isBalanced(root: Optional[TreeNode]) -> bool:
    def checkBalance(node):
        if not node:
            return 0, True

        leftHeight, leftBalance = checkBalance(node.left)
        rightHeight, rightBalance = checkBalance(node.right)

        currHeight = max(leftHeight, rightHeight) + 1
        currBalance = abs(leftHeight - rightHeight) <= 1 and leftBalance and rightBalance

        return currHeight, currBalance

    _, isBalanced = checkBalance(root)
    return isBalanced

#Leetcode Solution
#Visits each node exactly once, to get TC O(n), from bottom up
#simultaniosly get height of each subtree to make sure the differenc is < 1
#returns two values [boolBalanced, height]
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]



