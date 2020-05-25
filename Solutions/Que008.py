class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_trees(node):

    if not node: #null values--return 0
        return 0
    elif not node.right and not node.left: # if leaves then return 1
        return 1
    elif not node.right and node.data == node.left.data: #no right child and left child value is equal to root
        return 1 + count_trees(node.left)
    elif not node.left and node.data == node.right.data:  # no left child and right child value is equal to root
        return 1 + count_trees(node.right)

    subtree_count = count_trees(node.left) + count_trees(node.right)
    current_count =0
    if node.data == node.right.data and node.data == node.left.data:
        current_count = 1
    return current_count + subtree_count

node_a = Node('5')
node_b = Node('1')
node_c = Node('5')
node_d = Node('5')
node_e = Node('5')
node_f = Node('5')

node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.right = node_f

print(count_trees(node_a))