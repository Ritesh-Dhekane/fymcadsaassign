# Q14. Write a program to construct an Expression Tree from postfix expression.

print("Name= Ritesh Dhekane")

# Node class for expression tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to construct expression tree from postfix
def construct_expression_tree(postfix):
    stack = []
    
    for char in postfix:
        if char.isalnum():  # Operand
            stack.append(Node(char))
        else:  # Operator
            right = stack.pop()
            left = stack.pop()
            new_node = Node(char)
            new_node.left = left
            new_node.right = right
            stack.append(new_node)
    
    return stack.pop()  # Root of the expression tree

# Function to print inorder traversal of expression tree
def inorder(root):
    if root:
        if root.left or root.right:
            print("(", end="")
        inorder(root.left)
        print(root.data, end="")
        inorder(root.right)
        if root.left or root.right:
            print(")", end="")

# Example usage
postfix_expr = "ab+cde+**"
root = construct_expression_tree(postfix_expr)
print("Inorder traversal of the constructed expression tree:")
inorder(root)
print()
