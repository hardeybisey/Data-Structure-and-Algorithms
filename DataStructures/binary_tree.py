class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node:
                if current_node.data >= value:
                    # go left
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    # go right
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        if self.root is None:
            return False
        current_node = self.root
        while current_node:
            if current_node.data == value:
                return current_node
            elif current_node.data > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
        # while current_node:
        #     if current_node.data >= value:
        #         # go left
        #         if current_node.data == value:
        #             return current_node
        #         current_node = current_node.left
        #     else:
        #         # go right
        #         if current_node.data == value:
        #             return current_node
        #         current_node = current_node.right
        # return False


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.lookup(20)
print(tree)
