class Stack:
    def __init__(self):
        self.stack=[]
        self.max_stack=[]

    def push(self,data):
        self.stack.append(data)
        if not self.max_stack or data > self.stack[self.max_stack[-1]]:
            self.max_stack.append(len(self.stack)-1)


    def pop(self):
        if not self.stack:
            return None
        if len(self.stack) -1  == self.max_stack[-1]:
            self.max_stack.pop()

        return self.stack.pop()

    def max(self):
        if not self.stack:
            return None
        return self.stack[self.max_stack[-1]]

stack=Stack()
stack.push(1)
stack.pop()
stack.push(2)
stack.push(3)
print(stack.max())
stack.push(4)
stack.pop()
stack.push(5)
stack.push(6)
print(stack.max())
stack.push(7)
stack.pop()
stack.push(8)
print(stack.max())