print("Name= Ritesh Dhekane")

class Stack:
    def __init__(self, max_size):
        self.stack = [0] * max_size  # Pre-allocate array
        self.top = -1
        self.max_size = max_size

    def push(self, value):
        if self.top >= self.max_size - 1:
            print("Stack Overflow! Cannot push", value)
        else:
            self.top += 1
            self.stack[self.top] = value
            print(value, "pushed to stack")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow! Nothing to pop")
        else:
            popped_value = self.stack[self.top]
            self.top -= 1
            print(popped_value, "popped from stack")
            return popped_value

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements are:", end=" ")
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()

# Example usage
stack_size = 5
s = Stack(stack_size)

s.push(10)
s.push(20)
s.push(30)
s.display()

s.pop()
s.display()

s.push(40)
s.display()
