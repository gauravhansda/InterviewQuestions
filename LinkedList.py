class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found is False:
            print "{} not found in the linked list".format(item)

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        if self.isEmpty():
            self.add(item)
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        temp = Node(item)
        current.setNext(temp)

    def printLinkedList(self):
        current = self.head
        linked_list = []
        while current is not None:
            linked_list.append(current.getData())
            # linked_list =linked_list+" "+ str(current.getData())
            # print current.getData()
            current = current.getNext()
        print " ".join(map(str, linked_list))

    def reverse(self):
        current = self.head
        stack = Stack()
        while current:
            stack.push(current)
            current = current.getNext()
        print stack.size()

        current = stack.peek()
        self.head = current
        stack.pop()

        while not stack.isEmpty():
            current.setNext(stack.peek())
            stack.pop()
            current = current.getNext()
        current.setNext(None)


class LinkedList(object):
    head1 = None
    head2 = None

    def size(self,head):
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def getNode(self):
        c1 = self.size(LinkedList.head1)
        c2 = self.size(LinkedList.head2)

        if c1 > c2:
            d = c1 - c2
            return self.__getIntersectionNode(d, LinkedList.head1, LinkedList.head2)
        else:
            d = c2 - c1
            return self.__getIntersectionNode(d, LinkedList.head2, LinkedList.head1)

    def __getIntersectionNode(self, d, node1, node2):
        current1 = node1
        current2 = node2

        for i in range(d):
            current1 = current1.next

        while current1 is not None and current2 is not None:
            if current1.data == current2.data:
                return current1.data
            current1 = current1.next
            current2 = current2.next

        return -1

    def printLinkedList(self, head):
        current = head
        linked_list = []
        while current is not None:
            linked_list.append(current.getData())
            # linked_list =linked_list+" "+ str(current.getData())
            # print current.getData()
            current = current.getNext()
        print " ".join(map(str, linked_list))


def main_intersectionOfLinkedList():
    l = LinkedList()
    LinkedList.head1 = Node(3)
    LinkedList.head1.next = Node(6)
    LinkedList.head1.next.next = Node(9)
    LinkedList.head1.next.next.next = Node(15)
    LinkedList.head1.next.next.next.next = Node(30)

    # creating second linked list
    LinkedList.head2 = Node(10)
    LinkedList.head2.next = Node(15)
    LinkedList.head2.next.next = Node(30)

    l.printLinkedList(LinkedList.head1)
    l.printLinkedList(LinkedList.head2)

    print "The node of intersection is " + str(l.getNode())


mylist = UnorderedList()
mylist.add(3)
mylist.add(6)
mylist.add(2)
mylist.add(24)
mylist.add(14)
print "Original list:"
mylist.printLinkedList()
mylist.append(99)
print "After Appending:"
mylist.printLinkedList()
mylist.add(101)
mylist.append(22)
# mylist.printLinkedList()
# mylist.remove(23)
# print "After removing 6:"
mylist.printLinkedList()
print "after Reverse:"
mylist.reverse()
mylist.printLinkedList()

# if __name__ == '__main__':
#     main_intersectionOfLinkedList()
