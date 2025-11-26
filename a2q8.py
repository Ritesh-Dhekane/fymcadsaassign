# Q8. Write a Program to check for balanced parentheses by using Stacks.

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

    def is_empty(self):
        return self.top == -1

# Function to check balanced parentheses
def is_balanced(expr):
    n = len(expr)
    stack = Stack(n)
    
    # Mapping of closing to opening brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            if stack.pop() != brackets[char]:
                return False
    
    return stack.is_empty()

# Example usage
expression = "{[()()]}"
print("Expression:", expression)
if is_balanced(expression):
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")
