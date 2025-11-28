print("Name= Ritesh Dhekane")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        new_node.prev = temp

    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def delete_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.delete_beginning()
dll.delete_end()
dll.display()
