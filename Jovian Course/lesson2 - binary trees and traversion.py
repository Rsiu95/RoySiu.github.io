# Creating a class
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created!')
    
    # prints the information in the format User(username = xx, email = xx)
    def __repr__(self):
        return("User(username='{}', email='{}').".format(self.username, self.email))
    
    # returns the repr as a string
    def __str__(self):
        return self.__repr__()
    
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(guest_name, self.name, self.email))   

# Create a data structure which can store 100M records and perform insertion, search, update, and list operations efficiently
class UserDatabase:
    def __init__(self):
        self.users = []
    
    # Insert: loop through the list and add the new user at a position that keeps the list sorted
    def insert(self, user): # O(n)
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
            
        self.users.insert(i, user)
    
    # Find: loop through the list and find the user object with the username matching the query.
    def find(self, username): # O(n)
        for user in self.users:
            if user.username == username:
                return user
    
    # Update: loop through the list, find the user object matching the query and update the details
    def update(self, user): # O(n)
        target = self.find(user.username)
        if target:
            target.name, target.email = user.name, user.email
    
    # List: return the list of user objects
    def list_all(self): # O(1)
        return self.users

# Create UserDatabase object before creating User objects
database = UserDatabase()

john = User('john', 'John Doe', 'john@doe.com')
jeff = User('jeff', 'Jeff Jones', 'jeff@jones.com')
joe = User('joe', 'Joe Smith', 'joe@smith.com')
jelly = User('jelly', 'Jelly Fish', 'jelly@fish.com')
joel = User('joel', 'Joel Turd', 'joel@turd.com')
jeremy = User('jeremy', 'Jeremy Low', 'jeremy@low.com')
julie = User('julie', 'Julie Cho', 'julie@cho.com')
josh = User('josh', 'Josh Priest', 'josh@priest.com')
jordan = User('jordan', 'Jordan Rants', 'jordan@rants.com')

database.insert(john)
database.insert(jeff)
database.insert(joe)
database.insert(jelly)
database.insert(joel)
database.insert(jeremy)
database.insert(julie)
database.insert(josh)
database.insert(jordan)


user = database.find('john')
print(user)

database.update(User(username='john', name='John Siu', email='john@siu.com'))

user = database.find('john')

print(user)
print(database.list_all())
database.insert(jelly)

print(database.list_all())


# above is a brute force solution to insert/find/update/list in a database. This is a slow way to implement this. 
# it is possible to speed this process up

# binary search trees and traversion
# Implement a binary tree using Python, and show its usage with some examples

# constructor class to initialise the tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
# create the ndoes
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print(node0.key)
# assign the left and right node of node0
node0.left = node1
node0.right = node2

# assign root node
tree = node0

print(tree.key)

# print the nodes of the rood node
print(tree.left.key)
print(tree.right.key)
'''
'''
node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(5)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(6)
node8 = TreeNode(8)

node0.left = node1
node1.left = node2
node0.right = node3
node3.left = node4
node4.right = node5
node3.right = node6
node6.left = node7
node6.right = node8

'''

# above assignment is inconvenient
# write a helper function to convert a tuple with the structure (left_subtree, key, right_subtree) where left_subtree and right_subtree are also tuples themselves

#tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    
    # check if the input data is of length 3 and is in the form of a tuple
    if isinstance(data, tuple) and len(data) == 3:
        
        # Set index 1 to the parent node
        node = TreeNode(data[1])
        
        # recursively set the tuple values
        # set index 0 to be the left child node
        node.left = parse_tuple(data[0])
        # set index 2 to be the right childe node
        node.right = parse_tuple(data[2])

    # if there is no data, set the node to none        
    elif data is None:
        node = None
    else:
        # otherwise, the node is equal to the data
        node = TreeNode(data)
        
    return node

tree2 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
# check level 1
print(tree2.key)

# check level 2
print(tree2.left.key, tree2.right.key)

# check level 3
print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)

# check level 4
print(tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key)

# define a function that converts a tree to a tuple
def tree_to_tuple(node):
    if node is None:
        return None
    
    # recursively set the left and right values
    left_subtree = tree_to_tuple(node.left)
    right_subtree = tree_to_tuple(node.right)
    
    return (left_subtree, node, right_subtree)


def display_keys(node, space = '\t', level = 0):
    # print(node.key if node else None, level)
    
    # if the node is empty
    if node is None:
        print(space * level + 'x')
        return
    
    # if the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return
    
    # if the node has childeren
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    
    display_keys(node.left, space, level + 1)

display_keys(tree2, '       ')

# this display of the tree will produce a tree that looks like this:
#                      8
#               7
#                      6
#        5
#                      4
#               3
#                      x
# 2
#               x
#        3
#               1
#
# This is a -90 degree rotation of the tree

# more tree examples
tree3 = parse_tuple(((None, 1, (1, 3, 4)), 5, (((None, 2, None), 3, (None, 2, (4, 5, None))))))

display_keys(tree3, '       ')

#                             x
#                      5
#                             4
#               2
#                      x
#        3
#               2
# 5
#                      4
#               3
#                      1
#        1
#               x

# traversing a binary tree

# write a function to perform the inorder traversal of a binary tree.
# This means to traverse the left subtree recursively in order, traverse the current node, traverse the right subtree recursively in order.

#                      8
#               7
#                      6
#        5
#                      4
#               3
#                      x
# 2
#               x
#        3
#               1
#

# Here this means we will check the root, 2 and see if it has a left node, we see that it exists so we will traverse to 3 and see if it has a left node, we see that it does, so we traverse to 1
# and check if that has a left node, we see that it doesn't, so we see if it has a right node, and we see that it doesn't so we now return 1 or append it to a list and traverse back up to 3. We
# then check the right node of 3 since we've already visited the left node of 3. We see 3 has no right node, so we return 3, we then go back to 2 and apply the same logic. In terms of visiting
# the tree the order would be 1 > 3 > None > 2 > 3 > None > 4 > 5 > 6 > 7 > 8

# write a funciton to perform the perorder traversal of a binary tree.
# This means to traverse the current node, traverse the left subtree recursively preorder, traverse the right subtree recursively preorder
# 
#                      8
#               7
#                      6
#        5
#                      4
#               3
#                      x
# 2
#               x
#        3
#               1
#

# Here this means we traverse the root, return 2, then move and check for left and return 3, then check the left and return 1, check right of 1, check right of 3, check right of 5 then check left
# of 5, right of 3, right of 5, left of 7, right of 8
# returning in this order 2 > 3 > 1 > None > 5 > 3 > None > 4 > 7 > 6 > 8

# write a function to perform the postorder traversal of a binary tree
# This means to go as far left as possible, return the left tree, return its parent, return the right tree, return the right tree, return their parent
# 
#                      8
#               7
#                      6
#        5
#                      4
#               3
#                      x
# 2
#               x
#        3
#               1
#
# this means 1 > None > 3 > None > 4 > 3 > 6 > 8 > 7 > 5 > 2

# in order traversal
def traverse_in_order(node):
    if node is None:
        return []
    
    return(traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

print("traverse in order", traverse_in_order(tree2))

#  pre order traveral
def traverse_pre_order(node):
    if node is None:
        return []
    
    return([node.key] + traverse_pre_order(node.left) +  traverse_pre_order(node.right))
print("traverse pre order", traverse_pre_order(tree2))

# post order traversal
def traverse_post_order(node):
    if node is None:
        return []
    
    return(traverse_post_order(node.left) +  traverse_post_order(node.right) + [node.key])

print("traverse pre order", traverse_post_order(tree2))

# height of a binary tree
def tree_height(node):
    if node is None:
        return 0
    
    return 1 + max(tree_height(node.left), tree_height(node.right))

print("tree height =", tree_height(tree2))

# check number of nodes of tree
def tree_size(node):
    if node is None:
        return 0
    
    return 1 + tree_size(node.left) + tree_size(node.right)

print("tree size =", tree_size(tree2))

# "Encapsulation" of all the previous functions

class TreeNode():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        
    def height(self):
        if self is None:
            return 0
        
        return 1 + TreeNode.height(self.left) + TreeNode.height(self.right)
    
    def size(self):
        if self is None:
            return 0
        
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    
    def traverse_in_order(self):
        if self is None:
            return []
        
        return (TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right))
    
     
    def traverse_pre_order(self):
        if self is None:
            return []
        
        return ([self.key] + TreeNode.traverse_pre_order(self.left) + TreeNode.traverse_pre_order(self.right))
        
    def traverse_in_order(self):
        if self is None:
            return []
        
        return (TreeNode.traverse_post_order(self.left) + TreeNode.traverse_post_order(self.right) + [self.key])

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
    is_bst_node = (is_bst_left and is_bst_right and (max_left is None or node.key > max_left) and (max_right is None or node.key < min_right))
    
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
'''     
tree = BSTNode(jelly.username, jelly)

print(tree.key, tree.value)

tree.left = BSTNode(jeff.username, jeff)
tree.left.parent = tree
tree.right = BSTNode(joe.username, joe)
tree.right.parent = tree
tree.right.right = BSTNode(john.username, john)
tree.right.right.parent = tree.right

display_keys(tree)
'''
#                 john
#         joe
#                 x
# jelly
#         jeff

#print(is_bst(tree))

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

tree = insert(None, jelly.username, jelly)
insert(tree, jeff.username, jeff)
insert(tree, joe.username, joe)
insert(tree, john.username, john)

print(is_bst(tree))
display_keys(tree)

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

print(is_balanced(tree))

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

data = [(user.username, user) for user in database.users]
tree = make_balanced_bst(data)
display_keys(tree)

# balance an unbalanced BST
def balance_bst(node):
    return make_balanced_bst(list_all(node))

tree1 = None
for user in database.users:
    tree1 = insert(tree1, user.username, user)
    
display_keys(tree1)
tree2 = balance_bst(tree1)
display_keys(tree2)

# Time complexities
# Insert > O(log(n)) + O(n) >> O(n)
# Find > O(log(n))
# Update > O(log(n))
# List all > O(n)

class TreeMap():
    def __init__(self):
        self.root = None
        self.counter = 0

    " __setitem__ allows you to assign the key value by calling 'Treemap['john']' = john"        
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.counter += 1
            if self.counter > 99:
                self.root = balance_bst(self.root)
                self.counter = 0
        else:
            update(self.root, key, value)

    # __getitem__ allows you to call the node name by typing "TreeMap["john"]"
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    # __iter__ allows for the class to be used in a for loop 
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    # __len__ allows you to use the len() function on the tree
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)