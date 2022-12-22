class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def push(self, value):
        self.stack.append(value)
        return self

    def pop(self):
        self.stack.pop()
        return self


stack = Stack()
stack.push("I")
stack.push("Love")
stack.push("This")
stack.peek()
stack.pop()