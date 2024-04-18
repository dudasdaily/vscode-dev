# ?ž¬ê·?(recursion)
# ?“±ì°¨ìˆ˜?—´?˜ ?•©, ì´ˆí•­?´ 1?´ê³? ?“±ì°¨ê?? 3
def seq(n):

    if n == 1: # ê²½ê³„ì¡°ê±´, ì´ˆí•­?´ 1?ž„
        return 1

    else:
        return seq(n - 1) + 3

# ?”¼ë³´ë‚˜ì¹? ?ˆ˜?—´
def fib(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return fib(n - 1) + fib(n - 2)
    
# ?•˜?…¸?´?˜ ?ƒ‘
# nê°œì˜ ?›?Œ?„ start?—?„œ tempë¥? ê±°ì³ target?œ¼ë¡? ?´?™
def move(n, a, b):
    print(n,"ë²? ?›?Œ : ", a, " -> ", b)

def hanoi(n, start, target, temp):
    if n == 1:
        move(1, start, target)
        return

    else:
        hanoi(n-1, start, temp, target)
        move(n, start, target)
        hanoi(n-1, temp, target, start)

# ?„ ?ƒ ? •? ¬
# ìµœëŒ“ê°’ì„ ì°¾ê³  ê·? ê°’ê³¼ ? œ?¼ ?˜¤ë¥¸ìª½ ?•„?´?…œ?„ ë°”ê¿ˆ
def selectionSort(arr):
    if arr != []:
        x = max(arr)
        arr.remove(x)
        return selectionSort(arr) + [x]
    
    else:
        return []


# ?›?˜• ?—°ê²°ë¦¬?Š¤?Š¸
# class Node:
#     def __init__(self, item = None, next = None):
#         self.item = item
#         self.next = next
    
# class CircularList:
#     def __init__(self):
#         self.head = Node('dummy')
#         self.tail = Node(None, self.head)
#         self.numItems = 0
    

#     def getNode(self, i: int):
#         if self.numItems == 0 or i > self.numItems - 1:
#             print("Failed getNode()")
#             return None
        
#         else:
#             curr = self.head

#             for index in range(i + 1):
#                 curr = curr.next
            
#             return curr
        
#     def append(self, item):
#         newNode = Node(item, self.head)
#         self.tail = newNode


#         if self.numItems == 0:
#             self.head.next = newNode
#             self.numItems += 1

#         else:
#             curr = self.head

#             for i in range(self.numItems):
#                 curr = curr.next
            
#             curr.next = newNode
#             self.numItems += 1
    
#     def printList(self):
#         if self.numItems == 0:
#             print("no Item")
#             return None
            
#         curr = self.head
#         for i in range(self.numItems - 1):
#             curr = curr.next
#             print(curr.item, " -> ",end="")
        
#         print(curr.next.item)

#     def pop(self, *args):
#         if self.numItems == 0:
#             print("there is no Item in Array")
#             return None
        
#         if len(args) != 0:
#             i = args[0]
#             if i > self.numItems - 1:
#                 print("failed pop(), Out of bound")
#                 return None
        
#         if len(args) == 0 or i == -1:
#             prev = self.getNode(self.numItems - 2)
#             curr = prev.next
#             rtn = curr.item
#             prev.next = curr.next
#             self.tail = prev
#             self.numItems -= 1

#             return rtn
        
#         else:
#             prev = self.getNode(i - 1)
#             curr = prev.next
#             rtn = curr.item
#             prev.next = curr.next
#             self.numItems -= 1

#             if i == self.numItems - 1:
#                 self.tail = prev
            
#             return rtn
    
#     def insert(self, i: int, x):
#         if i > self.numItems:
#             print("failed insert(), Out of Bound")
#             return None
        
#         if self.numItems == 0:
#             self.append(x)

        
#         elif i + 1 == self.numItems:
#             self.append(x)
        
#         else:
#             prev = self.getNode(i - 1)
#             nextNode = prev.next
#             newNode = Node(x, nextNode)
#             prev.next = newNode
#             self.numItems += 1
    
#     def reverse(self):
#         if self.numItems == 0 or self.numItems == 1:
#             return
        
#         else:
#             prev = self.head.next
#             curr = prev.next

#             self.tail = prev
#             prev.next = self.head

#             while curr.next != self.head:
#                 tmp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = tmp
            
#             curr.next = prev
            
#             self.head.next = curr


class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next


class CDL:
    def __init__(self):
        self.head = Node('dummy')
        self.head.prev = self.head
        self.head.next = self.head
        self.tail = Node(None, None, self.head)
        self.numItems = 0

    def getNode(self, i: int):
        if self.numItems == 0:
            print("there is no Item in List")
            return None

        else:
            curr = self.head
            for index in range(i + 1):
                curr = curr.next

            return curr

    def append(self, item):
        newNode = Node(item)

        if self.numItems == 0:
            self.head.next = newNode
            self.head.prev = newNode
            newNode.prev = self.head
            newNode.next = self.head
            self.tail = newNode

            self.numItems += 1

        else:
            curr = self.getNode(self.numItems - 1)
            curr.next = newNode
            newNode.next = self.head
            newNode.prev = curr
            self.head.prev = newNode
            self.tail = newNode
            self.numItems += 1


a = CDL()
a.append(1)
print(a.numItems)














