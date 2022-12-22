class LinkedList:
    def __init__(self,value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self,value):
        new_node = {
            'value': value,
            'next': None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self,value):
        new_node = {
            'value': value,
            'next': None
        }
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1
        return self

linkedlist = LinkedList(10)
linkedlist.append(5)
linkedlist.append(16)
linkedlist.append(50)
print(linkedlist)
print(linkedlist.tail)
print(linkedlist.length)