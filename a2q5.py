# Q5. Write a Program to Implement Priority Queue.

print("Name= Ritesh Dhekane")

class PriorityQueue:
    def __init__(self):
        self.queue = []  # Each element will be a tuple (data, priority)

    def enqueue(self, data, priority):
        # Insert element based on priority (lower number = higher priority)
        new_item = (data, priority)
        if not self.queue:
            self.queue.append(new_item)
        else:
            inserted = False
            for i in range(len(self.queue)):
                if priority < self.queue[i][1]:  # Higher priority
                    self.queue.insert(i, new_item)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(new_item)
        print(f"{data} enqueued with priority {priority}")

    def dequeue(self):
        if not self.queue:
            print("Priority Queue Underflow! Nothing to dequeue")
            return None
        item = self.queue.pop(0)
        print(f"{item[0]} dequeued from priority queue")
        return item

    def display(self):
        if not self.queue:
            print("Priority Queue is empty")
        else:
            print("Priority Queue elements (data, priority):", end=" ")
            for item in self.queue:
                print(item, end=" ")
            print()

# Example usage
pq = PriorityQueue()
pq.enqueue("Task1", 3)
pq.enqueue("Task2", 1)
pq.enqueue("Task3", 2)
pq.display()

pq.dequeue()
pq.display()

pq.enqueue("Task4", 1)
pq.display()
