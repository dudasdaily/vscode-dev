class Node:
  def __init__(self, item, next=None, prev=None):
    self.item = item
    self.next = next
    self.prev = prev


class LinkedList:
  def __init__(self):
    self.head = Node(None, None, None)
    self.cnt = 1

  def insert(self, i:int, x:int):
    """insert x in ith element"""
    curr = Node(x, None, None)
    if i == 0:
      self.head = curr

    else:
      prev = self.getNode(i - 1)
      self.curr.prev = prev
      prev.next = curr  


  def delete(self, i):
    """delete ith element"""

  def printList(self):
    """여기에 코딩"""

  def getNode(self, i : int):
    curr = self.head

    for index in range(i):
      curr = curr.next
    return curr

    
a = LinkedList()

a.insert(0, 4)