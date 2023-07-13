"""
Efficiently searches for a key AND find the min and max elements, enumerate keys in sorted order, and look for successor and predecessor of each key

Similiar to arrays (keys stored in sorted order) but keys can be added and deleted efficiently
Keys must respect BST propery

Insertion, lookup, deletion worst case is O(n) - proporotional to height of tree. libraries take O(logn)
    Note: there are implementations of insert and delete that guarntee tree has height O(logn)
    Example: red-black trees since they require storing and updating additional data at tree nodes
    

Note: avoid putting mutable objects in BST

Both BST and hashtables use O(n) space (in practice BST uses slightly more)

Libraries:
    - Python doesn't come with a built-in BST library
    - sortedcontainers module is best in-class module for soreted sets and dictionaries
    
    - bintrees module implements sorted sets and sorted dictionaries using balanced BSTs
        insert(e) inserts ne element
        discard(e) removes e in BST if present
        min_item()/max_item() yields the smalles and largest key - value pair
        min_key()/max_key() yeild smallest and largest key in BST
        pop_min/pop_max() returns and removes smalles and largest key-value pair
        
        these operations take O(logn)
       
BST property:
    1. value of every node in left subtree is less than parent
    2. val of every node in right subtree is greater or eqaul to parent
    3. left and right subtrees of node are also Binary search trees
        

"""

class BST:
    def __init__(self, data=None, left=None, right=None): 
        self.data, self.left, self.right = data, left, right
    
    """"""""""""""""""""""""    
    #check if given value is present in BST
    def search_bst(self,tree, key):
        return (tree if not tree or tree.data == key else search_bst(tree.left, key)
                if key < tree.data else search_bst(tree.right, key))
    def is_root(self, p):
        #Return True if Position p represents the root of the tree."""
        return self.root() == p
   
    def height2(self, p):                  # time is linear in size of subtree
        #Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        #Return the height of the subtree rooted at Position p.
        #If p is None, return the height of the entire tree.
        
        if p is None:
        p = self.root()
        return self._height2(p)        # start _height2 recursion
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


    """--------------------------------------"""
    def insert(self, val):
        """
        Insert a value into the binary search tree.
        """
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        """
        Helper method for recursively inserting a value into the binary search tree.
        """
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def search(self, val):
        """
        Search for a value in the binary search tree and return the node containing the value.
        """
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        """
        Helper method for recursively searching for a value in the binary search tree.
        """
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)

    def delete(self, val):
        """
        Delete a value from the binary search tree.
        """
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        """
        Helper method for recursively deleting a value from the binary search tree.
        """
        if node is None:
            return None

        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor_parent = node
                successor = node.right
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left
                if successor_parent != node:
                    successor_parent.left = successor.right
                    successor.right = node.right
                successor.left = node.left
                return successor

        return node
    
    """---------------------------------------------"""

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:          # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                               # visit p between its subtrees
        if self.right(p) is not None:         # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other
                
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)
         
    """-------------------------------------"""   
    def depth_first_search(self):
        if self.root is None:
            return []

        result = []
        self._dfs_recursive(self.root, result)

        return result

    def _dfs_recursive(self, node, result):
        if node is None:
            return

        result.append(node.val)
        self._dfs_recursive(node.left, result)
        self._dfs_recursive(node.right, result)
    
    def breadth_first_search(self):
        if self.root is None:
            return []

        result = []
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
    
def modulo_bst(nums, mod):
    # Create an instance of the BST class
    bst = BST()

    # Insert the numbers into the binary search tree
    for num in nums:
        bst.insert(num)

    # Perform modulo operation on each number in the binary search tree
    result = []
    inorder_nums = bst.inorder_traversal()
    for num in inorder_nums:
        result.append(num % mod)

    return result

# Example usage
nums = [17, 8, 29, 35, 16]
mod = 10

result = modulo_bst(nums, mod)
print(result)