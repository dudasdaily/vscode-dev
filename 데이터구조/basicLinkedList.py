class ListNode:
    def __init__(self, newItem, newNode : 'ListNode'):
        self.item = newItem
        self.next = newNode


class LinkedList:
    def __init__(self):
        self.head = ListNode(None, None)
        self.cnt = 0
    

    def getNode(self, i:int):
        curr = self.head

        for index in range(i):
            curr = curr.next

        return curr

    def insert(self, i : int, x):
        newNode = ListNode(x, None)

        if i == 0:
            self.head = newNode
    
        else:
            prev = self.getNode(i-1)
            prev.next = newNode
        
        self.cnt += 1

    def delete(self, i : int):
        if i == 0:
            self.head.item = None
        
        else:
            prev = self.getNode(i - 1)
            prev.next = None
        
        self.cnt -= 1

    
    def printList(self):
        curr = self.head

        for i in range(self.cnt):
            if i != self.cnt - 1:
                print(curr.item, end = ' -> ')
                curr = curr.next
            
            else:
                print(curr.item)
                curr = curr.next
        
             

a = LinkedList()

a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)
a.delete(2)

a.printList()

                            
