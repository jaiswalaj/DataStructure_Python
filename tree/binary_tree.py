# Solution of Question 1.1
# Class for creating Binary Tree with Left, Key and Right Nodes
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Solution of Question 1.1
# Converts the given data of Standard Tuple format in Binary Tree.
def parse_tuple_to_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple_to_tree(data[0])
        node.right = parse_tuple_to_tree(data[2])
    elif data == None:
        node = None
    else:
        node = TreeNode(data)

    return node


# Solution of Question 1.2
# Displays given Binary Tree in Tree View (Might have some issues with spaces printed on same level)
def display_tree(tree, list_data = []):

    # For displaying white spaces between nodes of same level
    def print_spaces(space_count):
        while space_count > 0:
            print(" ", end='')
            space_count = space_count - 1

    # For displaying nodes in a particular level and returning a list of all the nodes in the level below
    def display_tree_level(treenode_list, space_count):
        new_list = []
        
        for treenode in treenode_list:
            if treenode:
                print_spaces(space_count)
                print(treenode.key, end=' ')
                print_spaces(space_count)    
                if isinstance(treenode.left, TreeNode):
                    new_list.append(treenode.left)
                elif treenode.left is None:
                    new_list.append(None)

                if isinstance(treenode.right, TreeNode):
                    new_list.append(treenode.right)
                elif treenode.right is None:
                    new_list.append(None)
            else:
                print_spaces(space_count)
                print("None", end=' ')
                print_spaces(space_count)

        return new_list
    
    # For initializing the list containing all nodes of current level to be displayed for the first time
    if len(list_data) == 0:
        list_data = display_tree_level([tree], 70)
        print("\n")
    
    # For updating the list containing all nodes of next level to be displayed
    while len(list_data) > 0:
        list_data = display_tree_level(list_data, 70 // len(list_data))
        print("\n")


# Solution of Question 1.3
# Converts the given Binary Tree in Standard Tuple format.
def parse_tree_to_tuple(tree):

    # For checking if the given node is a sub tree or just a node
    def is_tree(subtree):
        if subtree.left or subtree.right:
            return True
        else:
            return False

    # For parsing left side of the given tree into tuple
    if tree.left is None:
        left_tuple = (None)
    elif is_tree(tree.left):
        left_tuple = parse_tree_to_tuple(tree.left)
    else:
        left_tuple = (tree.left.key)

    # For parsing right side of the given tree into tuple
    if tree.right is None:
        right_tuple = (None)
    elif is_tree(tree.right):
        right_tuple = parse_tree_to_tuple(tree.right)
    else:
        right_tuple = (tree.right.key)

    # Returning the final tuple with left, key, and right tree data inplace
    return (left_tuple, tree.key, right_tuple)


# Solution of Question 2.1
# Inorder Tree Traversal
def inorder_tree_traversal(tree):
    if tree.left:
        inorder_tree_traversal(tree.left)
    
    print(tree.key, end='  ')

    if tree.right:
        inorder_tree_traversal(tree.right)


# Solution of Question 2.2
# Preorder Tree Traversal
def preorder_tree_traversal(tree):
    print(tree.key, end='  ')

    if tree.left:
        preorder_tree_traversal(tree.left)

    if tree.right:
        preorder_tree_traversal(tree.right)


# Solution of Question 2.3
# Postorder Tree Traversal
def postorder_tree_traversal(tree):
    if tree.left:
        postorder_tree_traversal(tree.left)

    if tree.right:
        postorder_tree_traversal(tree.right)

    print(tree.key, end='  ')


# Sample Binary Tree
# Uncomment following variety of tree and create the tree from given tuple or vice versa
tree = parse_tuple_to_tree((((8, 4, 10), 1, (13, 6, None)), 2, ((None, 5, 12), 3, (11, 7, 9))))
# tree = parse_tuple_to_tree((((6, 1, 4), 3, (9, 8, 7)), 2, ((8, 7, 6), 8, (6, 4, 2))))
# tree = parse_tuple_to_tree((((2, 0, 9), 3, (5, 4, 3)), 1, ((4, 5, 8), 6, (7, 8, 0))))
# tree = parse_tuple_to_tree((((8, 5, 2), 5, None), 5, (7, 4, 3)))
# tree = parse_tuple_to_tree(((3, 2, None), 1, (None, 4, 5)))


# Displaying Solutions

print("\nDisplaying the Binary Tree: \n")
display_tree(tree)

tuple_data = parse_tree_to_tuple(tree)
print("\nStandard Tuple Format: ", tuple_data, "\n\n")

print("\nInorder Tree Traversal: ")
inorder_tree_traversal(tree)
print("\n")

print("\nPreorder Tree Traversal: ")
preorder_tree_traversal(tree)
print("\n")

print("\nPostorder Tree Traversal: ")
postorder_tree_traversal(tree)
print("\n")
