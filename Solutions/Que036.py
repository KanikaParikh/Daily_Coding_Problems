# BST - left child < parent < right child
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def second_largest_node(root):
    if root.right:

        max_node = root
        second_max_node = None

        while max_node.right:
            second_max_node = max_node
            max_node = max_node.right

        if max_node.left:
            second_max_node = max_node.left

            while second_max_node.right:
                second_max_node = second_max_node.right
        return second_max_node.data


    elif root.left:
        second_max_node = root.left
        while second_max_node.right:
            second_max_node = second_max_node.right
        return second_max_node.data

    else:
        return None


"""
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 11
             \     
              12

 """
BST = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(11,None,Node(12)))))
print(second_largest_node(BST))
