# Q9. Write a program to convert infix expression into postfix expression.

print("Name= Ritesh Dhekane")

class Stack:
    def __init__(self, max_size):
        self.stack = [0] * max_size
        self.top = -1
        self.max_size = max_size

    def push(self, value):
        if self.top >= self.max_size - 1:
            print("Stack Overflow! Cannot push", value)
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

# Function to define precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

# Function to convert infix to postfix
def infix_to_postfix(expression):
    stack = Stack(len(expression))
    postfix = ""
    
    for char in expression:
        if char.isalnum():  # Operand
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '('
        else:  # Operator
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(char)):
                postfix += stack.pop()
            stack.push(char)
    
    # Pop remaining operators
    while not stack.is_empty():
        postfix += stack.pop()
    
    return postfix

# Example usage
infix_expr = "A+B*(C^D-E)"
print("Infix Expression:", infix_expr)
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)
