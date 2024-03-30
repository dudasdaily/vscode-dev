class ListNode:
    def __init__(self, newItem, nextNode):
        self.item = newItem
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.head = ListNode('dummy', None)

    def __getNode(self):
        