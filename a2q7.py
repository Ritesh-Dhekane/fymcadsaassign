# Q7. Write a Program to reverse a string using stack.

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
            print("Stack Underflow! Nothing to pop")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

# Function to reverse a string using stack
def reverse_string(s):
    n = len(s)
    stack = Stack(n)
    
    # Push all characters to stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from stack to get reversed string
    reversed_str = ""
    for i in range(n):
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage
input_str = "Ritesh"
print("Original String:", input_str)
reversed_str = reverse_string(input_str)
print("Reversed String:", reversed_str)
