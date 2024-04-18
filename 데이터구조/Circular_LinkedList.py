class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    

class Circular:
    # 더미헤드는 자기 자신을 가리키고, 테일은 헤드를 가리킴
    def __init__(self):
        self.head = Node('dummy')
        self.tail = Node()
        self.head.next = self.head
        self.tail.next = self.tail
        self.numItems = 0
    
    # 인자로 준 i번째 노드를 반환
    def getNode(self, i: int):
        curr = self.head

        # curr이 (i - 1)번째 노드가 될때까지 반복
        while i > 0:
            curr = curr.next
            i -= 1
        
        return curr.next
    

    def append(self, x):
        newNode = Node(x, self.head)

        if self.numItems == 0:
            self.tail = newNode
            self.head.next = self.tail
            self.numItems += 1
            return None
        
        self.tail.next = newNode
        self.tail = newNode
        self.numItems += 1

    
    def printList(self):
        curr = self.head.next

        while curr.next != self.head:
            print(curr.item)
            curr = curr.next
        
        print(curr.item)


    def pop(self, *args):
        if self.numItems == 0:
            print("there is no item in array")
            return None        

        if len(args) != 0:
            i = args[0]

        if len(args) != 0 and i > self.numItems - 1:
            print("failed pop(), Out of bound!")
            return None

        # 인자를 안 준 경우
        if len(args) == 0 or i == -1:
            prev = self.getNode(self.numItems - 2)
            rtn = prev.next.item
            prev.next = self.head
            self.tail = prev
            self.numItems -= 1

            return rtn
        

        
        

             
        
        


        
    

a = Circular()

a.append(1)
print(a.pop())
a.append(3)
a.pop(0)

a.printList()