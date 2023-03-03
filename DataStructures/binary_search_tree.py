class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self,name=''):
        self.root = None
        self.name = name
    
    def add(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return self
        else:
            current_node = self.root
            while current_node:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return self 
                    else:     
                        current_node  = current_node.left
                elif data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    else:
                        current_node = current_node.right
                else:
                    return self       

    def search(self, value):
        if self.root is None:
            return 'Empty Tree'
        current_node = self.root
        while current_node:
            if current_node.data < value:  # go right
                current_node = current_node.right
            elif current_node.data > value:  # go left
                current_node = current_node.left
            else:  # found the root
                print('Found it!!')
                return current_node
        return 'Not found!!'
    
    def traversePreorder(self, root, array = []):
        array.append(root.data)
        if root.left:
            self.traversePreorder(root.left, array)
        if root.right:
            self.traversePreorder(root.right, array)
        return array
    
    def traverseInorder(self, root, array = []):
        if root.left:
            self.traverseInorder(root.left, array)
        array.append(root.data)
        if root.right:
            self.traverseInorder(root.right, array)
        return array
    
    def traversePostorder(self, root, array = []):
        if root.left:
            self.traversePostorder(root.left, array)
        if root.right:
            self.traversePostorder(root.right, array)
        array.append(root.data)
        return array
    
    def height(self,root, h=0):
        leftHeight = self.height(root.left, h+1) if root.left else h
        rightHeight = self.height(root.right, h+1) if root.right else h
        return max(leftHeight,rightHeight)

    def getNodeAtDepth(self, tree, depth, nodes=[]):
        if depth == 0:
            nodes.append(tree.data)
            return nodes
        if tree.left:
            self.getNodeAtDepth(tree.left, depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        if tree.right:
            self.getNodeAtDepth(tree.right, depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes
    
    def _nodeToChar(self, n , spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing - len(str(n))+ 1
        return str(n)+ (' '*spacing) 
    
    def printTree(self):
        height = self.height(self.root)
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                print( ' '*(offset+1) + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\'] *(2**(depth-1))))
            row = self.getNodeAtDepth(self.root, depth , [])
            print((' '* offset) + ''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset/2) - 1
        print('')
        
    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        return root.data
    
    def deleteNode(self, root, target):
        if root is None:
            return root   
        
        if target < root.data and root.left:
            root.left = self.deleteNode(root.left, target)

        elif target > root.data and root.right:
            root.right = self.deleteNode(root.right, target)

        else: # target == root.data
            if root.right and root.left:
                minValue = self.findMin(root.right)
                root.data = minValue
                root.right = self.deleteNode(root.right, minValue)
            else:
                return root.right or root.left
            
        return root
        

tree = Tree()
tree.add(50)
tree.add(25)
tree.add(75)
tree.add(67)
tree.add(100)
tree.add(120)
tree.add(80)
tree.add(92)
# tree.add(50)
# tree.add(25)
# tree.add(75)
# tree.add(10)
# tree.add(35)
# tree.add(5)
# tree.add(13)
# tree.add(30)
# tree.add(42)
# tree.add(2)