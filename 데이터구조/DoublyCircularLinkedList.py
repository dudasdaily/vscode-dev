class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = Node('dummy')
        self.head.prev = self.head
        self.head.next = self.head
        self.tail = Node(None, self.head, self.head)
        self.numItems = 0

    def append(self, x):
        newNode = Node(x, self.head.prev, self.head)
        self.head.prev.next = newNode
        self.head.prev = newNode
        self.tail = newNode
        self.numItems += 1
    
    def getNode(self, i: int):
        if i == self.numItems - 1:
            return self.tail
        
        else:
            curr = self.head
            for index in range(i + 1):
                curr = curr.next
            return curr
    
    def pop(self, *args):
        if self.numItems == 0:
            print('there is no Item in List')
            return None
        
        if len(args) != 0:
            i = args[0]
            if i > self.numItems - 1:
                print("failed pop(), Out of Bounds")
                return None
        
        if len(args) == 0 or i == -1:
            curr = self.tail
            prev = self.tail.prev
            rtn = curr.item

            prev.next = curr.next
            self.tail = prev
            self.head.prev = self.tail
            self.numItems -= 1
        
        else:
            prev = self.getNode(i - 1)
            curr = prev.next
            next = curr.next
            rtn = curr.item

            prev.next = next
            next.prev = prev

            if i == self.numItems -1:
                self.tail = prev

            self.numItems -= 1
            return rtn
    
    def insert(self, i: int, x):
        if i > self.numItems:
            print("failed insert(), Out of Bounds!")
            return None

        if i == self.numItems:
            self.append(x)
        
        else:
            curr = self.getNode(i)
            prev = curr.prev

            newNode = Node(x, prev, curr)
            prev.next = newNode
            curr.prev = newNode
            self.numItems += 1



        


    
    def printList(self):
        if self.numItems == 0:
            print("there is no Item in List")
            return None
        
        else:
            curr = self.head

            while(curr != self.tail):
                curr = curr.next
                if curr == self.tail:
                    print(curr.item)
                else:
                    print(curr.item, " -> ", end='')
