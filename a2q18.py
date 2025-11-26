# Q18. Given a Binary Search Tree and an integer ‘K’. 
# Write a program to find and return the ‘K-th’ smallest and ‘K-th’ largest element in the given Binary Search Tree.

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

    # Insert node
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    # Inorder traversal to get sorted elements
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.data)
            self.inorder(root.right, result)

    # Find K-th smallest and largest
    def kth_smallest_largest(self, root, k):
        result = []
        self.inorder(root, result)
        n = len(result)
        if k > n or k <= 0:
            return None, None
        kth_smallest = result[k-1]
        kth_largest = result[n-k]
        return kth_smallest, kth_largest

# Example usage
bst = BST()
root = None
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    root = bst.insert(root, elem)

k = 3
k_small, k_large = bst.kth_smallest_largest(root, k)
print(f"{k}-th Smallest element:", k_small)
print(f"{k}-th Largest element:", k_large)
