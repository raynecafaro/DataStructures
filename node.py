"""
    Author: Rayne Cafaro
    File: node.py
    Description: A node class to be used
        for data structure implementations.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def main():
    Test1 = Node('test1')
    Test2 = Node('test2')
    Test3 = Node('test3')
    Test4 = Node('test4')

    Test1.next = Test2
    Test2.next = Test3
    Test3.next = Test4
    
    start = Test1

    while start:
        print(start.data)
        start = start.next

if __name__ == "__main__":
    main()
