class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        if self.length == 0:
            return None
        if self.first == self.last:
            self.last = None
        temp = self.first
        self.first = self.first.next
        self.length -= 1
        return self


queue = Queue()
queue.enqueue('Python')
queue.enqueue('Java')
queue.enqueue('Sql')
queue.dequeue()
queue.peek()
