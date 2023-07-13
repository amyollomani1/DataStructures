# input is a binary tree. check if tree statisfies BST propery

#TC is O(n) and additional SC is O(h)
#inorder traversal visits keys in sorted order

def is_binary_tree_bst(tree, low_range=float(’-inf’), high_range=float(’inf’)): 
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and
    is_binary_tree_bst(tree.right, tree.data, high_range))