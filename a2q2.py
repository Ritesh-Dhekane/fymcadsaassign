print("Name= Ritesh Dhekane")

# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Points to the top node of the stack

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(value, "pushed to stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow! Nothing to pop")
            return None
        popped_value = self.top.data
        self.top = self.top.next
        print(popped_value, "popped from stack")
        return popped_value

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Stack elements are:", end=" ")
            current = self.top
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

s.pop()
s.display()

s.push(40)
s.display()
