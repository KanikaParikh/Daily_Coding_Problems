
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False

    def is_lock(self):
        return self.locked

    # check whether the node is parent or not
    def check_parent(self):

        if self.locked:
            return False

        # none means no parent hence it is root so true
        if self.parent == None:
            return True

        return self.parent.check_parent()

    def check_child(self):

        if self.locked:
            return False

        return (not self.left or self.left.check_child()) and \
               (not self.right or self.right.check_child())

    def lock_node(self):

        if self.locked:
            return False

        if (not self.parent or self.parent.check_parent()) or (
                (not self.left or self.left.check_child()) and (not self.right or self.right.check_child())):
            self.locked = True
            print("Node Locked: " + str(self.data))
            return True

        print("Cannot Lock Node: " + str(self.data))
        return False

    def unlock_node(self):

        if self.locked == False:
            return False

        if (not self.parent or self.parent.check_parent()) or (
                (not self.left or self.left.check_child()) and (not self.right or self.right.check_child())):
            self.locked = False
            print("Node Unlocked: " + str(self.data))
            return True

        print("Cannot Unlock Node: " + str(self.data))
        return False


"""
       4
      / \
     2   5
    / \
   1   3
  /
 0
"""

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

four.left = two
two.parent = four

four.right = five
five.parent = four

two.left = one
one.parent = two

two.right = three
three.parent = two

one.left = zero
zero.parent = one

two.lock_node()
zero.lock_node()
one.lock_node()
zero.unlock_node()
one.lock_node()
zero.lock_node()
one.unlock_node()
two.unlock_node()
one.unlock_node()
zero.unlock_node()

'''
Node Locked: 2
Node Locked: 0
Cannot Lock Node: 1
Node Unlocked: 0
Node Locked: 1
Node Locked: 0
Cannot Unlock Node: 1
Node Unlocked: 2
Node Unlocked: 1
Node Unlocked: 0
'''