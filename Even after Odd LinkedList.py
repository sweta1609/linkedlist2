from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    #Your code goes here
    even = None
    odd = None
    o = None
    e = None
    while head:
        if head.data%2 == 0:
            if even == None:
                even = head
                e = head
            else:
                e.next = head
                e = e.next
        else:
            if odd == None:
                odd = head
                o = head
            else:
                o.next = head
                o = o.next
        head = head.next 
    if (o) :
      o.next = even
    if(e):
        e.next = None
    if (o):
        return odd
    return even
    
    
    
      









#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
