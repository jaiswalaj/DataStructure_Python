class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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


# Converts the given Binary Tree in Standard Tuple format.
def parse_tree_to_tuple(tree):
    def is_tree(subtree):
        if subtree.left or subtree.right:
            return True
        else:
            return False

    if tree.left is None:
        left_tuple = (None)
    elif is_tree(tree.left):
        left_tuple = parse_tree_to_tuple(tree.left)
    else:
        left_tuple = (tree.left.key)

    if tree.right is None:
        right_tuple = (None)
    elif is_tree(tree.right):
        right_tuple = parse_tree_to_tuple(tree.right)
    else:
        right_tuple = (tree.right.key)

    return (left_tuple, tree.key, right_tuple)


def display_tree(tree, list_data = []):
    def print_spaces(space_count):
        while space_count > 0:
            print(" ", end='')
            space_count = space_count - 1

    def display_subtree(treenode_list, space_count):
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
    
    
    if len(list_data) == 0:
        list_data = display_subtree([tree], 70)
        print("\n")
    
    while len(list_data) > 0:
        list_data = display_subtree(list_data, 70 // len(list_data))
        print("\n")
    









# Uncomment following variety of tree and create the tree from given tuple or vice versa
# tree = parse_tuple_to_tree((((8, 4, 10), 1, (13, 6, None)), 2, ((None, 5, 12), 3, (11, 7, 9))))
# tree = parse_tuple_to_tree((((6, 1, 4), 3, (9, 8, 7)), 2, ((8, 7, 6), 8, (6, 4, 2))))
# tree = parse_tuple_to_tree((((2, 0, 9), 3, (5, 4, 3)), 1, ((4, 5, 8), 6, (7, 8, 0))))
# tree = parse_tuple_to_tree((((8, 5, 2), 5, None), 5, (7, 4, 3)))

tree = parse_tuple_to_tree(((3, 2, None), 1, (None, 4, 5)))

tuple_data = parse_tree_to_tuple(tree)
print(tuple_data)

display_tree(tree)
