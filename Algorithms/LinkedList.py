
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def toString(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        return self

    def prepend(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        return self

    def printSentinel(self):
        curr = self.head
        while curr is not None:
            if curr.next is not None:
              print(curr.toString(), end='->')
            else:
                print(curr.toString(), end='->null')
            curr = curr.next


    def printList(self):
        curr = self.head.next
        while curr is not None:
            if curr.next is not None:
              print(curr.toString(), end='->')
            else:
                print(curr.toString(), end='->null')
            curr = curr.next


list = LinkedList()

list.append(1)
list.append(2)
list.append(5)
list.append(7)

list.prepend(10)


list.printList()

print('\n')

list.printSentinel()




