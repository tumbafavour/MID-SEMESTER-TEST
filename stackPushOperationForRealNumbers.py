class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

stack = Stack()
stack.push(5)
stack.push(4)
stack.push(10)
