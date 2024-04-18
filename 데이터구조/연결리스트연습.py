# item�씠�옉 next瑜� 媛�吏� �겢�옒�뒪
class Node:
    def __init__(self, newItem = None, nextNode = None):
        self.item = newItem
        self.next = nextNode

class LinkedList:
    def __init__(self):
        # head �뒗 none|none �쑝濡� 珥덇린�솕
        self.head = Node()
        self.numItems = 0

    # 由ъ뒪�듃 鍮꾩뿀�쑝硫� True 由ы꽩
    def is_empty(self):
        if self.numItems == 0:
            return True
            
        else:
            return False

    # 由ъ뒪�듃 �걹�뿉 x瑜� 異붽��
    def append(self, x):
        # 鍮덈━�뒪�듃硫� head瑜� x濡� 珥덇린�솕
        if self.is_empty():
            self.head = Node(x)

        # 鍮덈━�뒪�듃 �븘�땲硫� prev瑜� �뿤�뱶濡� 珥덇린�솕 �븯怨� prev�쓽 next瑜� x濡� 珥덇린�솕
        else:
            prev = self.head
            for i in range(self.numItems - 1):
                prev = prev.next

            prev.next = Node(x)
        
        self.numItems += 1
    
    # 由ъ뒪�듃�쓽 i踰덉㎏ �씤�뜳�뒪 �끂�뱶瑜� 由ы꽩
    def getNode(self, i : int):
        # 鍮� 由ъ뒪�듃硫� None由ы꽩        
        if self.is_empty():
            print("there is no item in list!")
            return None
        
        # 0�쓣 �씤�옄濡� 二쇰㈃ �뿤�뱶瑜� 由ы꽩
        if i == 0:
            return self.head
        
        # i >= 1, self.numItems >= 1 �씤 寃쎌슦, i踰덉㎏ �씤�뜳�뒪瑜� 由ы꽩
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            
            return curr
    
    # 由ъ뒪�듃 泥ル쾲吏� �끂�뱶遺��꽣 �걹�끂�뱶源뚯�� 異쒕젰
    def printList(self):
        if self.is_empty():
            print("there is no item in list!")
            return None
        
        else:
            curr = self.head
            while curr.next != None:
                print(curr.item, " -> ", end = "")
                curr = curr.next
            
            # curr.next == None�씪 寃쎌슦
            print(curr.item)

    def pop(self, *args):
        # 鍮덈━�뒪�듃�씤 寃쎌슦
        if self.is_empty():
            print("there is no item in list!")
            return None
                
        # �끂�뱶 1媛� �엳�쓣 寃쎌슦, �씠嫄� �븞�벐硫� prev.next.next媛� �뾾�뒗 寃쎌슦媛� �엳�뼱�꽌 �뿉�윭�쑑�닔�룄..?
        if self.numItems == 1:
            temp = self.head
            self.head.item = None
            self.numItems -= 1
            return temp

        # �씤�옄瑜� 以ъ쓣 �븣 i瑜� �씤�옄濡� 珥덇린�솕
        if len(args) != 0:
            i = args[0]
        
        # 由ъ뒪�듃�뿉 �뾾�뒗 �씤�뜳�뒪瑜� �씤�옄濡� 以� 寃쎌슦
        if len(args) != 0 and self.numItems - 1 < i:
            print("failed pop(),out of bound!")
            return None
        
        # numItems > 1, �씤�옄瑜� �븞以ъ쓣 寃쎌슦
        if len(args) == 0 or i == -1:
            prev = self.head

            while prev.next.next != None:
                prev = prev.next
            
            temp = prev.next.item
            prev.next = None

            self.numItems -= 1
            return temp
        
        # numItems > 1, �씤�옄瑜� 以�寃쎌슦
        else:
            prev = self.getNode(i - 1)
            curr = prev.next
            temp = curr.item
            prev.next = curr.next
            self.numItems -= 1

            return temp


class SingleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, i: int, x):
        # �끂�뱶 1媛쒕쭔 �엳�쓣寃쎌슦
        if self.numItems == 1:
            self.head.next = Node(x)
            self.numItems += 1
            return None


        # 鍮� 由ъ뒪�듃�씪 寃쎌슦
        if self.is_empty():
            self.head = Node(x)
            self.numItems += 1       
            return None

        # numItems > 1 �씠怨� i == 0 �씪 寃쎌슦
        elif i == 0:
            temp = self.head
            self.head = Node(x, temp)
            self.numItems += 1
            return None

        else:
            prev = self.getNode(i - 1)
            curr = Node(x, prev.next)
            prev.next = curr
            self.numItems += 1
            return None
        
    def reverse(self):
        newNode = SingleLinkedList()
        while self.numItems != 0:
            newNode.append(self.pop())
        
        for i in range(newNode.numItems - 1):
            self.insert(0, )

        
            

a = SingleLinkedList()

a.printList()
a.insert(0, 2)
a.printList()


a.insert(1, 1)
a.insert(0, 1)
a.printList()




