# Q4. Write a Program to Implement Linear Queue using Array.

print("Name= Ritesh Dhekane")

class Queue:
    def __init__(self, max_size):
        self.queue = [0] * max_size  # Pre-allocate array
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def enqueue(self, value):
        if self.rear >= self.max_size - 1:
            print("Queue Overflow! Cannot enqueue", value)
        else:
            if self.front == -1:  # First element
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
            print(value, "enqueued to queue")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow! Nothing to dequeue")
        else:
            dequeued_value = self.queue[self.front]
            self.front += 1
            print(dequeued_value, "dequeued from queue")
            # Reset pointers if queue becomes empty
            if self.front > self.rear:
                self.front = self.rear = -1
            return dequeued_value

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements are:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

# Example usage
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

q.enqueue(40)
q.display()
