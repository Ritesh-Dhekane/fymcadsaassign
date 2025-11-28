print("Name= Ritesh Dhekane")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_zero_sum(self):
        prev = None
        current = self.head
        while current:
            if current.data == 0:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                prev = current
            current = current.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

ll = LinkedList()
ll.append(10)
ll.append(0)
ll.append(-5)
ll.append(0)
ll.delete_zero_sum()
ll.display()
