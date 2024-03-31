class Node:
  def __init__(self, item, next=None, prev=None):
    self.item = item
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.cnt = 0

  def getNode(self, i : int):
    curr = self.head

    for index in range(i):
       curr = curr.next
    
    return curr
       

  def insert(self, i:int, x:int):
    """insert x in ith element"""
    if i == 0 and self.cnt == 0: # 0번째 인덱스에 집어 넣는데 헤드가 없는 경우
      self.head = Node(x)
    
    elif i == 0 and self.cnt != 0: # 0번째 인덱스에 집어 넣는데 헤드가 있는 경우
      curr = Node(x)
      curr.next = self.head
      self.head.prev = curr
      self.head = curr



    else:
      prevNode = self.getNode(self.cnt - 1)
      curr = Node(x, prevNode.next, prevNode)
      prevNode.next = curr
      
    self.cnt += 1


      

  def delete(self, i : int):
    if i == 0 and self.cnt == 0:
      print('there is no element in list!!')
      return None
    
    prevNode = self.getNode(i - 1)
    curr = prevNode.next

    if i == 0 and self.cnt != 0:
      self.head = self.head.next
      self.head.prev = None
    
    

    
    else:
      prevNode.next = curr.next
      curr.prev = None
      curr.next = None

    self.cnt -= 1  


  def printList(self):
    if self.cnt == 0:
      print('end'); return None

    curr = self.head

    for i in range(self.cnt):
      print(curr.item, end = ' -> ')
      curr = curr.next
    
    print('end')
    
        
a = LinkedList()

a.insert(0, 1)
a.insert(1, 2)
a.delete(0)
a.insert(0, 1)
a.insert(2, 3)
a.insert(3, 4)
a.printList()