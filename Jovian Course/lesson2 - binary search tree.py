# A Binary search tree (BST) is a bianry tree that satisfies the following conditions:
#   1. The left subtree of any node only contains nodes with keys less than the node's key
#   2. The right subtree of any node only contains nodes with keys greater than the node's key
#   3. each child of a binary search tree must also satisfy the condtions for a BST

# write a function to check if a binary tree is a BST
# write a function to find the maximum key in a binary tree
# write a function to find the minimum key in a binary tree

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    
    # returns True if there is no tree
    if node is None:
        return True, None, None
    
    # recursively checks the left and right nodes of the tree
    is_bst_left, min_left, max_left = is_bst(node.left)
    is_bst_right, min_right, max_right = is_bst(node.right)
    
    # checking if the tree satisfies the BST condition
    is_bst_node = (is_bst_left and is_bst_right and (max_left is None or node.key > max_left) \
        and (max_right is None or node.key < min_right))
    
    # set values for min/max key
    min_key = min(remove_none([min_left, node.key, min_right]))
    max_key = max(remove_none([max_left, node.key, max_right]))
    
    # return if it's a BST, min key and max key
    return is_bst_node, min_key, max_key

# storing key-value pairs using BSTs
class BSTNode():
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
#tree = BSTNode(james.username, james)

#print(tree.key, tree.value)

# insert a new node into a BST

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
        
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
        
    return node

# find the value associated with a given key in a bst

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
    
# write a function to update the value associated with a given key within a bst

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

# write a function to retrieve all the key-values pairs stored in a BST in the sorted order of keys
# different way of asking for "inorder traversal"
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

# write a function to determine if a binary tree is balanaced
# recursive strategy:
# 1. ensure that the left subtree is balanced
# 2. ensure the right subtree is balanced
# 3. ensure that the difference between heights of left and right subtree is not more than 1

def is_balanced(node):
    if node is None:
        return True, 0
    
    balanced_left, height_left = is_balanced(node.left)
    balanced_right, height_right = is_balanced(node.right)
    if balanced_left and balanced_right and abs(height_left - height_right) <= 1:
        balanced = True
    #balanced = balanced_left and balanced_right and abs(height_left - height_right) <= 1
    height = 1 + max(height_left, height_right)
    return balanced, height

# write a function to create a balanced BST from a sorted list/array of key-value pairs.

def make_balanced_bst(data, lo = 0, hi = None, parent = None):
    if hi is None:
        hi = len(data) - 1
        
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]
    
    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)
    
    return root