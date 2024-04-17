# item이랑 next를 가진 클래스
class Node:
    def __init__(self, newItem = None, nextNode = None):
        self.item = newItem
        self.next = nextNode

class LinkedList:
    def __init__(self):
        # head 는 none|none 으로 초기화
        self.head = Node()
        self.numItems = 0

    # 리스트 비었으면 True 리턴
    def is_empty(self):
        if self.numItems == 0:
            return True

        else:
            return False

    # 리스트 끝에 x를 추가
    def append(self, x):
        # 빈리스트면 head를 x로 초기화
        if self.is_empty():
            self.head = Node(x)

        # 빈리스트 아니면 prev를 헤드로 초기화 하고 prev의 next를 x로 초기화
        else:
            prev = self.head
            for i in range(self.numItems - 1):
                prev = prev.next

            prev.next = Node(x)

        self.numItems += 1

    # 리스트의 i번째 인덱스 노드를 리턴
    def getNode(self, i : int):
        # 빈 리스트면 None리턴
        if self.is_empty():
            print("there is no item in list!")
            return None

        # 0을 인자로 주면 헤드를 리턴
        if i == 0:
            return self.head

        # i >= 1, self.numItems >= 1 인 경우, i번째 인덱스를 리턴
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next

            return curr

    # 리스트 첫번째 노드부터 끝노드까지 출력
    def printList(self):
        if self.is_empty():
            print("there is no item in list!")
            return None

        else:
            curr = self.head
            while curr.next != None:
                print(curr.item, " -> ", end = "")
                curr = curr.next

            # curr.next == None일 경우
            print(curr.item)

    def pop(self, *args):
        # 빈리스트인 경우
        if self.is_empty():
            print("there is no item in list!")
            return None

        # 노드 1개 있을 경우, 이거 안쓰면 prev.next.next가 없는 경우가 있어서 에러뜰수도..?
        if self.numItems == 1:
            temp = self.head
            self.head = Node()
            self.numItems -= 1
            return temp.item

        # 인자를 줬을 때 i를 인자로 초기화
        if len(args) != 0:
            i = args[0]

        # 0을 인자로 줬을경우
        if len(args) != 0 and i == 0:
            prev = self.head
            temp = prev.next

            self.head = temp
            self.numItems -= 1
            return prev.item


        # 리스트에 없는 인덱스를 인자로 줄 경우
        if len(args) != 0 and self.numItems - 1 < i:
            print("failed pop(),out of bound!")
            return None

        # numItems > 1, 인자를 안줬을 경우
        if len(args) == 0 or i == -1:
            prev = self.head

            while prev.next.next != None:
                prev = prev.next

            temp = prev.next.item
            prev.next = None

            self.numItems -= 1
            return temp

        # numItems > 1, 인자를 준경우
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

    # i번째에 노드를 삽입
    def insert(self, i: int, x):
        # 노드 1개만 있을경우
        if self.numItems == 1:
            self.head.next = Node(x)
            self.numItems += 1
            return None


        # 빈 리스트일 경우
        if self.is_empty():
            self.head = Node(x)
            self.numItems += 1
            return None

        # numItems > 1 이고 i == 0 일 경우
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
        tempList = SingleLinkedList()
        
        while self.numItems > 0:
            tempList.append(self.pop())

        while tempList.numItems > 0:
            self.append(tempList.pop(0))
            


a = SingleLinkedList()
a.append(1)
a.append(2)
a.append(3)
a.printList()

a.reverse()
a.printList()


