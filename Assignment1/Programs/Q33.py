print("Name= Ritesh Dhekane")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for i in range(pos-2):
            if temp is None:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

ll = LinkedList()
ll.insert_at_position(10,1)
ll.insert_at_position(20,2)
ll.insert_at_position(30,2)
ll.display()
