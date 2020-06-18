class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def nthfromlast(self, n):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)


l = LinkedList()
l.add_node(10)
l.add_node(8)
l.add_node(7)
l.add_node(3)
l.add_node(0)
l.nthfromlast(2)
