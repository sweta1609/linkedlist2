from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
    if i == j :
        return head
        
    currentNode = head
    prev = None
    
    firstNode = None 
    secondNode = None
    firstNodePrev = None
    secondNodePrev = None

    pos = 0

    while currentNode is not None :
        if pos == i :
            firstNodePrev = prev
            firstNode = currentNode
        elif pos == j:
            secondNodePrev = prev
            secondNode = currentNode

        prev = currentNode
        currentNode = currentNode.next
        pos += 1


    if firstNodePrev is not None :
        firstNodePrev.next = secondNode
    else :
        head = secondNode

    if secondNodePrev is not None :
        secondNodePrev.next = firstNode
    else :
        head = firstNode

    currentfirstNode = secondNode.next
    secondNode.next = firstNode.next
    firstNode.next = currentfirstNode

    return head



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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
