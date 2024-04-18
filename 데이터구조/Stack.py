from DoublyCircularLinkedList import DoublyLinkedList
from DoublyCircularLinkedList import Node

class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.top = Node()
    
    def pop(self, *args):
        super().pop(*args)
        self.top = self.tail

a = Stack()

a.append(1)
a.append(2)

a.pop(0)
a.printList()
