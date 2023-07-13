class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#recursive DFS Solution
#TC = O(n) where n is number of nodes
#SC = O(h) where h is height. worse case height of binary tree equals number of nodes resulting in O(n) SC

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)

    return max(left_depth, right_depth) + 1

#BFS Solution
#BFS usually uses Queue

"""
BFS ex
    3
   9   20
      15 7
Queue in BFS:
3 - level 1
replace with children: 9 20 : L2
replace 9 with children: 20 (since 9 has no children)
replace 20 with children: 15 17: L3

"""
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    level = 1
    q = deque([root])
    while q:
        for i in range(len(q)): #traverse level
            node = q.popleft()
            #append children
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level +=1
    return level

"""
Iterative DFS
Here we will be using preorder: process (pop) left subtree first
DFS uses a stack

     3  
   9   20
      15 7
      
start with 3
pop 3
add 20 then 9
pop 9
get its children (none since 9 doesn't have children)
now pop 20

add 7 and 15
process 15, pop it
then 7 is remaining pop it



"""
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    stack = [[root,1]] #we are storing node and depth at same time
    res = 1
    
    while stack:
        node,depth = stack.pop()
        if node:
            res = max(res,depth)
            stack.apped([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    
    return res