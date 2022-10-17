# Binary Tree

## Question 1

Use Python to implement a Binary Tree and carry out the following operations:
1. Save data in a Binary Tree from Standard Tuple format.
2. Present the Binary Tree in the best way feasible.
3. Output a Binary Tree in Standard Tuple Format after receiving it as an input.

<br/>

>### Standard Tuple format
>In this format, the `left child` of a binary tree is the first element, the `right child` is the last element, and the `root` node is represented as the second element of a three element long tuple. The final tuple will have tuples within them if the children are not `leaves`, in which case they can also be expressed using the same format.

            2 
           / \
          1   3
         / \ / \
        4  5 6 7

In Standard Tuple format, the Binary Tree seen here looks like this: `((4, 1, 5), 2, (6, 3, 7))`

<br/>

## Question 2

Write functions in python which will take a Binary Tree as input and perform following operations:
1. Inorder Tree Traversal
2. Preorder Tree Traversal
3. Postorder Tree Traversal

<br/>
