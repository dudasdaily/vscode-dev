class Node:
    def __init__(self, newItem = None, nextNode = None):
        self.item = newItem
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.numItems = 0

    def is_empty(self):
        if self.numItems == 0:
            return True
            
        else:
            return False

    def append(self, x):
        if self.is_empty():
            self.head = Node(x)

        else:
            prev = self.head
            for i in range(self.numItems - 1):
                prev = prev.next

            prev.next = Node(x)
        
        self.numItems += 1
    
    def getNode(self, i : int):
        if self.numItems == 0:
            print("there is no item in list!")
            return None

        if i == 0:
            return self.head

        prev = self.head
        for idx in range(i - 1):
            prev = prev.next
        
        return prev.next
    
    def pop(self, *args):
        if self.numItems == 0:
            print('there is no item in list!'); return None

        if len(args) != 0:
            i = args[0]

        if i >= self.numItems:
            print("out of bound")
            return None

        if len(args) == 0 or i == -1:
            if self.numItems == 1:
                rtn = self.head.item
                self.head.item = None
                self.numItems -= 1
                return rtn
            
            prev = self.getNode(self.numItems - 2)
            rtn = prev.next.item
            prev.next = None
            self.numItems -= 1
            return rtn        
        
        if i == 0:
            rtn = self.head.item
            self.head = self.head.next
            self.numItems -= 1
            return rtn
        
        else:
            prev = self.getNode(i - 1)
            curr = prev.next
            rtn = curr.item
            prev.next = curr.next
            self.numItems -= 1
            return rtn
             


