class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LList:
    def __init__(self):
        self.head = None


# creating an empty LL

LL = LList()
LL.head = Node("Surja")
sec = Node("Rohit")
third = Node("Mohit")
fourth = Node("Chandan")

LL.head.next = sec
sec.next = third
third.next = fourth


# Now we'll be traversing
def printList():
    val = LL.head
    while val:
        if val.next:
            print("Value= ", val.value, end=", ")
        else:
            print("Value= ", val.value)
        val = val.next


printList()


# insterting a new node at the head of the Linked List

def changeHead(value):
    newHead = Node(value)
    newHead.next = LL.head
    LL.head = newHead


changeHead("Mohor")
printList()


# inserting a node after a certain Node

def insertNode(where, what):
    val = LL.head
    newNode = Node(what)
    while (val):
        if val.value == where:
            newNode.next = val.next
            val.next = newNode
            break
        if val.next is None:
            print(" No such element found")
            break
        val = val.next
    printList()


insertNode("Mohit", "Dada")
