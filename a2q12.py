# Q12. Write a program to count the total number of nodes in a binary tree.

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

    # Function to count total nodes
    def count_nodes(self, root):
        if root is None:
            return 0
        left_count = self.count_nodes(root.left)
        right_count = self.count_nodes(root.right)
        return 1 + left_count + right_count

# Example usage
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

total_nodes = bt.count_nodes(bt.root)
print("Total number of nodes in the binary tree:", total_nodes)
