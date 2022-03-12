from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def reverseLinkedListRec(head) :
	#Your code goes here
    if head is None or head.next is None:
        return head
    
    smallHead = reverseLinkedListRec(head.next)
    '''
    curr = smallHead
    while curr.next is not None:
        curr = curr.next
    '''
    head.next.next = head
    head.next = None
    return smallHead


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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = reverseLinkedListRec(head)
    printLinkedList(newHead)

    t -= 1
