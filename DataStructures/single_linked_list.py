class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        self.length += 1
        return self

    def print_list(self):
        array = []
        current_node = self.head
        while current_node:
            array.append(current_node.data)
            current_node = current_node.next
        return array

    def traverse_list(self, index):
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def insert(self, index, data):
        if index >= self.length:
            return self.append(data)
        if index == 0:
            return self.prepend(data)
        new_node = Node(data)
        prev_node = self.traverse_list(index - 1)
        curr_node = prev_node.next
        new_node.next = curr_node
        prev_node.next = new_node
        self.length += 1
        return self

    def remove(self, index):
        if index >= self.length:
            raise IndexError("list index out of range")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return self

        prev_node = self.traverse_list(index - 1)
        del_node = prev_node.next
        prev_node.next = del_node.next
        self.length -= 1
        return self

    def reverse(self):
        if self.length == 1:
            return self
        curr_node = self.head
        next_node = curr_node.next
        self.tail = self.head
        while next_node:
            temp = next_node.next
            next_node.next = curr_node
            curr_node = next_node
            next_node = temp
        self.head.next = None
        self.head = curr_node
        return self


linkedlist = LinkedList()
linkedlist.append(16)
linkedlist.append(50)
linkedlist.prepend(5)
linkedlist.prepend(1)
linkedlist.insert(3, 90)
linkedlist.remove(0)
print(linkedlist.print_list())
linkedlist.reverse()
print(linkedlist.print_list())