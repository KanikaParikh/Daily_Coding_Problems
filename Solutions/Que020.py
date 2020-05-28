class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def intersecting_node(A, B):
    visited_node = set()

    current_node = A

    while current_node != None:
        visited_node.add(id(current_node))
        current_node = current_node.next

    current_node = B
    while current_node != None:
        current_node_ID = id(current_node)
        if current_node_ID in visited_node:
            return current_node.data
        visited_node.add(current_node_ID)

        current_node=current_node.next

    return None

interesect_node = Node(4, Node(5))
A = Node(3, Node(7, Node(8,interesect_node)))
B = Node(99, Node(7, interesect_node))
print(intersecting_node(A, B))
