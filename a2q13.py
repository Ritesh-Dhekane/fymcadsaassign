# Q13. Write a program to find the height (or depth) of a binary tree.

print("Name= Ritesh Dhekane")

# Node class for binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Function to find the height of the tree
    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

# Example usage
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

tree_height = bt.height(bt.root)
print("Height (or depth) of the binary tree:", tree_height)
