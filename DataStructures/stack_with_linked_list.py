class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.top

    def push(self, value):
        new_item = Node(value)
        if self.top is None:
            self.top = new_item
            self.bottom = new_item
        else:
            new_item.next = self.top
            self.top = new_item
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None
        if self.top == self.bottom:
            self.bottom = None
        retrieved = self.top
        self.top = retrieved.next
        self.length -= 1
        return self


stack = Stack()
stack.push("I")
stack.push("Love")
stack.push("This")
stack.peek()
stack.pop()