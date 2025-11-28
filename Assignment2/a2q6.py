# Q6. Write a Program to Implement Circular Queue.

print("Name= Ritesh Dhekane")

class CircularQueue:
    def __init__(self, max_size):
        self.queue = [0] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def enqueue(self, value):
        # Check for overflow
        if (self.front == 0 and self.rear == self.max_size - 1) or (self.rear + 1) % self.max_size == self.front:
            print("Circular Queue Overflow! Cannot enqueue", value)
        else:
            if self.front == -1:  # First element
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            print(value, "enqueued to circular queue")

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue Underflow! Nothing to dequeue")
            return None
        dequeued_value = self.queue[self.front]
        if self.front == self.rear:  # Queue becomes empty
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        print(dequeued_value, "dequeued from circular queue")
        return dequeued_value

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty")
        else:
            print("Circular Queue elements are:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size
            print()

# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()

cq.dequeue()
cq.display()

cq.enqueue(60)
cq.display()
