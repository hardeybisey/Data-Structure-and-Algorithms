class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
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
        move_node = prev_node.next
        new_node.next = move_node  # configure the new node next pointer
        new_node.prev = prev_node  # configure the new node previous pointer
        prev_node.next = new_node
        move_node.prev = new_node
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
        prev_node.prev = del_node.prev
        self.length -= 1
        return self


linkedlist = DoublyLinkedList()
linkedlist.append(10)
linkedlist.append(5)
linkedlist.append(16)
linkedlist.prepend(1)
linkedlist.insert(1, 6)
linkedlist.remove(3)
linkedlist.print_list()
