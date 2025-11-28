print("Name= Ritesh Dhekane")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def merge_sorted_dll(h1, h2):
    dummy = Node(0)
    tail = dummy
    while h1 and h2:
        if h1.data < h2.data:
            tail.next = h1
            h1.prev = tail
            h1 = h1.next
        else:
            tail.next = h2
            h2.prev = tail
            h2 = h2.next
        tail = tail.next
    while h1:
        tail.next = h1
        h1.prev = tail
        tail = tail.next
        h1 = h1.next
    while h2:
        tail.next = h2
        h2.prev = tail
        tail = tail.next
        h2 = h2.next
    if dummy.next:
        dummy.next.prev = None
    return dummy.next

def print_dll(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

a1 = Node(1)
a1.next = Node(3)
a1.next.prev = a1
a1.next.next = Node(5)
a1.next.next.prev = a1.next

a2 = Node(2)
a2.next = Node(4)
a2.next.prev = a2
a2.next.next = Node(6)
a2.next.next.prev = a2.next

merged = merge_sorted_dll(a1, a2)
print_dll(merged)
