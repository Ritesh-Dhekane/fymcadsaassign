# Q10. Write a program to create a binary search tree, insert, and delete an element from binary search tree.

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

    # Find the minimum value node in BST
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

# Example usage
bst = BST()
root = None

# Insert elements
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    root = bst.insert(root, elem)

print("Inorder Traversal of BST after insertion:")
bst.inorder(root)
print()

# Delete a node
root = bst.delete(root, 50)
print("Inorder Traversal of BST after deleting 50:")
bst.inorder(root)
print()
