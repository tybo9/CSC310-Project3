import random
def create2D(n):
    A  = [[' ']*n for i in range(n)]
    B =  [[' ']*n for i in range(n)]
    sum =0
    for i in range(n):
        for j in range(n):
            #Populate the array using random values from 0 to 255
            A[i][j] = random.randint(0,255)
            #sum of each value in the array to find its mean
            sum = sum + A[i][j]
            #Transpose of A
            B[j][i] = A[i][j]
    #mean value of all the elements in the array
    mean = sum/(n*n)
    for i in range(n):
        for j in range(n):
            #subtract mean from each element of B
            B[i][j] = B[i][j] - int(mean)
    return B

print("Modified B: ",create2D(3))



#4th question: Create a linked list class
class LinkedList:
    #Inner class called Node
    class _Node:
        def __init__(self, element, next):  #Initialise node's field
            self._element = element     #Reference to integer
            self._next = next           #Reference to next Node in the list

    def __init__(self):     #Initialise LinkedList
        self._head = None   #Head of the list
        self._size = 0      #Reference to size of the list

    def insertAtHead(self, element):
        self._head = self._Node(element, self._head)    #Create a new node with the value as element and next as head of the list
        self._size = self._size + 1     #increase the size, as a element is added

    def insertAtEnd(self, element):
        head = self._head
        newNode = self._Node(element, None)
        if(self._size == 0):
            self._head = newNode
            self._size = self._size + 1
            return
        while(head._next!=None):    #Loop untill you get the last element of the linkedlist
            head = head._next
        head._next = newNode  #create a new node and assign it to last element
        self._size = self._size + 1

    def countElements(self):    #Count the number of elements in list
        return self._size

    def maxElement(self):   #Return maximum element in list
        temp = self._head
        max = temp._element
        while(temp != None):    #loop through all the element of list to find the maxinum
            if(max < temp._element):
                max = temp._element
            temp = temp._next
        return max

    def print(self):    #print all the elements in the list
        temp = self._head
        while(temp != None):
            print(temp._element, end=" ")
            temp = temp._next
        print(" ")



linkedList  =  LinkedList()

for i in range(5):
    linkedList.insertAtHead(random.randint(0,10))

print("The elements in the list: ", end = " ")
linkedList.print()
print("Number of elements: ", linkedList.countElements())
print("Maximum element: ",linkedList.maxElement())

#Question 5
def mergeAndSort(listA,listB):
    headA = listA._head
    headB = listB._head
    mergedList = LinkedList()   #used to store combined sorted lists
    while(headA != None and headB != None):     #loop through both the list
        if(headA._element < headB._element):    #if value in listA is less that listB, add listA value to mergedList
            mergedList.insertAtEnd(headA._element)
            headA = headA._next     #move to the next node of listA
        else:
            mergedList.insertAtEnd(headB._element)  # add listB value to sortedList
            headB = headB._next  # move to the next value of listA
    # Add the remaining values from both the list
    while(headA!=None):
        mergedList.insertAtEnd(headA._element)
        headA = headA._next
    while (headB != None):
        mergedList.insertAtEnd(headB._element)
        headB = headB._next
    return mergedList

listA = LinkedList()
listA.insertAtEnd(1)
listA.insertAtEnd(3)
listA.insertAtEnd(5)
print("ListA: ", end = " ")
listA.print()
listB = LinkedList()
listB.insertAtEnd(2)
listB.insertAtEnd(4)
listB.insertAtEnd(6)
print("ListB: ", end = " ")
listB.print()

finalList = mergeAndSort(listA,listB)
print("Merged List: ", end = " ")
finalList.print()



