import sys

class Node:
    def __init__(self, key= None):
        self.key = key
        self.next = self.prev = self #한방향 연결 리스트와는 달리, 빈 리스트의 이전, 이후 노드가 모두 자기 자신을 가리킨다.

    def __str__(self):
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __iter__(self):
        v = self.head.next
        while v  != self.head:
            yield v
            v = v.next
    def __str__(self):
        return ''.join(str(v.key) for v in self)

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        
        ap = a.prev
        bn = b.next

        # cut a to b
        ap.next = b.next
        bn.prev = a.prev

        # insert a to b after x

        xn = x.next
        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b

    def moveAfter(self, a, x): #노드 a를 노드 x 뒤로 이동
        self.splice(a,a,x)

    def moveBefore(self, a, x): #노드 a를 노드 x 앞으로 이동
        self.splice(a,a,x.prev)

    def insertAfter(self, x, key): # x뒤에 데이터가 key인 새 노드 생성하여 삽입
        self.moveAfter(Node(key),x)

    def insertBefore(self, x, key): # x 앞에 데이터가 key인 새 노드 생성하여 삽입
        self.moveBefore(Node(key),x)

    def pushFront(self, key): # 데이터 key인 새 노드 생성 -> head 다음에 삽입
        self.insertAfter(self.head, key)

    def pushBack(self, key): # 데이터 key인 새 노드 생성 -> head 이전에 삽입
        self.insertBefore(self.head, key)

    def remove(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next #링크 변경
        x.next.prev = x.prev
        del x

    def popFront(self): #head 다음에 있는 노드 값 리턴
        if self.isEmpty():
            return None
        key = self.head.next.key
        self.remove(self.head.next)
        return key

    def popBack(self):
        if self.isEmpty(): #head 이전에 있는 노드 값 리턴
            return None
        key = self.head.prev.key
        self.remove(self.head.prev)
        return key


L = DoublyLinkedList()

cursor = Node('|')
cursor.next = L.head
cursor.prev = L.head
L.head.next = cursor
L.head.prev = cursor

text = list(sys.stdin.readline().strip())

for i in text:
  L.insertBefore(cursor, i)

N = int(sys.stdin.readline().strip())

for i in range(N):
    command = sys.stdin.readline().strip()

    if command[0]== "L" and cursor.prev.key!=None :
        L.moveBefore(cursor, cursor.prev)
    elif command[0]=="D" and cursor.next.key!=None:
        L.moveAfter(cursor, cursor.next)
    elif command[0]=="B" and cursor.prev.key!=None:
        L.remove(cursor.prev)
    elif command[0]== "P":
        L.insertBefore(cursor, command[2])

L.remove(cursor)

print(L)