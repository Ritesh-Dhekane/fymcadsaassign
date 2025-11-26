# Q3. Write a Program to Implement Linear Queue using linked list.

print("Name= Ritesh Dhekane")

# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(value, "enqueued to queue")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow! Nothing to dequeue")
            return None
        dequeued_value = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue became empty
            self.rear = None
        print(dequeued_value, "dequeued from queue")
        return dequeued_value

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Queue elements are:", end=" ")
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

q.enqueue(40)
q.display()
