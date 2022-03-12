from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''
MergeSort(headRef)
1) If the head is NULL or there is only one element in the Linked List 
    then return.
2) Else divide the linked list into two halves.  
      FrontBackSplit(head, &a, &b); /* a and b are two halves */
3) Sort the two halves a and b.
      MergeSort(a);
      MergeSort(b);
4) Merge the sorted a and b (using SortedMerge() discussed here) 
   and update the head pointer using headRef.
     *headRef = SortedMerge(a, b);
'''

        
        
def sortedMerge( a, b):
        result = None
         
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
             
        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = sortedMerge(a.next, b)
        else:
            result = b
            result.next =sortedMerge(a, b.next)
        return result
     
def mergeSort(head) :
	#Your code goes here
    # Base case if head is None
    if head == None or head.next == None:
        return head
 
        # get the middle of the list
    middle = getMiddle(head)
    nexttomiddle = middle.next
 
        # set the next of middle node to None
    middle.next = None
 
        # Apply mergeSort on left list
    left = mergeSort(head)
         
        # Apply mergeSort on right list
    right = mergeSort(nexttomiddle)
 
        # Merge the left and right lists
    sortedlist = sortedMerge(left, right)
    return sortedlist

def getMiddle(head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow




























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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
