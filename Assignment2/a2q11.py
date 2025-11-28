# Q11. Write a program to implement binary search tree traversal operations- Inorder, Preorder, and Postorder.

print("Name= Ritesh Dhekane")

# Node class for BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BST class
class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    # Inorder traversal (Left, Root, Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder traversal (Root, Left, Right)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal (Left, Right, Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

# Example usage
bst = BST()
root = None

# Insert elements
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    root = bst.insert(root, elem)

print("Inorder Traversal:")
bst.inorder(root)
print("\nPreorder Traversal:")
bst.preorder(root)
print("\nPostorder Traversal:")
bst.postorder(root)
print()
