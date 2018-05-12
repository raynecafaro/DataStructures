from node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def lprint(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insert_head(self, data=None):
        second = None
        if self.head is not None:
            second = self.head
        
        self.head = Node(data)

        if second:
            self.head.next = second

    def append(self, data=None):
        if self.head is None:
            self.insert_head(data) 
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = Node(data)

class DoubleLinkedList:
    def __init__(self, head = None):
        self.head = head

    def lprint(self):
        curr = self.head
        while curr:
            print(node.data)
            curr = curr.next

    def insert_head(self, data=None):
        second = None
        if self.head is not None:
            second = self.head
        
        self.head = Node(data)

        if second:
            self.head.next = second
            second.prev = self.head

    def append(self, data=None):
        if self.head is None:
            self.insert_head(data) 
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = Node(data)
        curr.next.prev = curr

def single_test():
    Lst = LinkedList()
    
    # Test insert_head()
    Lst.head = Node("First Node")
    Lst.lprint()
    Lst.insert_head("Better First Node")
    Lst.lprint()

    # Test append()
    Lst.append('Appended Element')
    Lst.lprint()

    # Test append() on fresh list
    NewList = LinkedList()
    NewList.append("Hello")
    NewList.lprint()

def double_test():
    pass

def main():
    single_test()
    double_test()

if __name__ == "__main__":
    main()
