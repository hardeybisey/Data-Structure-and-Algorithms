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
            if current_node.data < value:  # go right
                current_node = current_node.right
            elif current_node.data > value:  # go left
                current_node = current_node.left
            else:  # found the node
                return current_node
        return False
    
    def bfs(self):
        curr_node = self.root
        array = []
        queue = []
        queue.append(curr_node)
        while len(queue) > 0:
            curr_node = queue.pop(0)
            array.append(curr_node.data)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        return array
    
    def traverseInorder(self, node, array = []):
        if node.left:
            self.traverseInorder(node.left, array)
        array.append(node.data)
        if node.right:
            self.traverseInorder(node.right, array)
        return array
    
    def traversePreorder(self, node, array = []):
        array.append(node.data)
        if node.left:
            self.traversePreorder(node.left, array)
        if node.right:
            self.traversePreorder(node.right, array)
        return array
    
    def traversePostorder(self, node, array = []):
        if node.left:
            self.traversePostorder(node.left, array)
        if node.right:
            self.traversePostorder(node.right, array)
        array.append(node.data)
        return array
    
    
    def remove(self, value):
        if self.root is None:
            return False
        current_node = self.root
        prev_node = None
        while current_node:
            if current_node.data > value:  # go left
                prev_node = current_node
                current_node = current_node.left
            elif current_node.data < value:  # go right
                prev_node = current_node
                current_node = current_node.right
            else:  # found the node
                if current_node.right is None:  # option 1 no right child
                    if prev_node is None:
                        self.root = current_node.left
                    else:
                        # if prev_node > current_node, make current_node left a left child of prev_node
                        if current_node.data < prev_node.data:
                            prev_node.left = current_node.left
                        # if prev_node < current_node, make current_node left child a right child of prev_node
                        elif current_node.data > prev_node.data:
                            prev_node.right = current_node.left

                elif current_node.right.left is None:  # option 2
                    if prev_node is None:
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left
                        # //if prev_node > current_node, make right child of the left the prev_node
                        if current_node.data < prev_node.data:
                            prev_node.left = current_node.right
                        # //if prev_node < current_node, make right child a right child of the prev_node
                        elif current_node.data > prev_node.data:
                            current_node.right = current_node.right

        #     #Option 3: Right child that has a left child
        #     else:
        #         #find the Right child's left most child
        #         leftmost = currentNode.right.left
        #         leftmostParent = currentNode.right
        #         while leftmost.left != None:
        #             leftmostParent = leftmost
        #             leftmost = leftmost.left
        #
        #         #Parent's left subtree is now leftmost right subtree
        #         leftmostParent.left = leftmost.right
        #         leftmost.left = currentNode.left
        #         leftmost.right = currentNode.right
        #
        #         if parentNode == None:
        #             self.root = leftmost
        #         else:
        #             if currentNode.data < parentNode.data:
        #                 parentNode.left = leftmost
        #             elif currentNode.data > parentNode.data:
        #                 parentNode.right = leftmost
        # return True


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.lookup(20)
tree.remove(170)
# tree.bfs()
# tree.traverseInorder(tree.root)
# tree.traversePreorder(tree.root)
# tree.traversePostorder(tree.root)
