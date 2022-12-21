class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def remove(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item


newArray = MyArray()
newArray.push("I")
newArray.push("Love")
newArray.push("Coding")
print(newArray)
