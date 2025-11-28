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

    def count(self):
        temp = self.head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("Number of nodes:", ll.count())
