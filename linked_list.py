from node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def lprint(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def insert_head(self, data=None):
        second = None
        if self.head is not None:
            second = self.head
        
        NewNode = Node(data)
        self.head = NewNode

        if second:
            self.head.next = second

    def append(self, data=None):
        pass 
        
def single_test():
    Lst = LinkedList()
    Lst.head = Node("Beginning")

    # Create the Nodes
    # node2 = Node("Second")
    # node3 = Node("Third")
    # node4 = Node("Fourth")
    # node5 = Node("Last")

    # Link the Nodes
    #Lst.head.next = node2
    #node2.next = node3
    #node3.next = node4
    #node4.next = node5

    Lst.lprint()
    Lst.insert_head("New Beginning")
    Lst.lprint()

def double_test():
    pass

def main():
    single_test()
    double_test()

if __name__ == "__main__":
    main()
