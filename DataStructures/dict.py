class MyDict:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash_no = 0
        for i in range(len(key)):
            hash_no = (hash_no + ord(key[i]) * i) % self.size
        return hash_no

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = [[key, value]]
        else:
            self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        for i in range(len(current_bucket)):
            if (current_bucket[i][0]) == key:
                return current_bucket[i][1]

    def keys(self):
        dict_keys = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    pass
                    for j in range(len(self.data[i])):
                        dict_keys.append(self.data[i][j][0])
                else:
                    dict_keys.append(self.data[i][0][0])
        return dict_keys

    def values(self):
        dict_values = []
        for i in range(len(self.data)):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        dict_values.append(self.data[i][j][1])
                else:
                    dict_values.append(self.data[i][0][1])
        return dict_values


mydict = MyDict(5)
mydict.set('grapes', 1000)
mydict.set('apple', 54)
mydict.set('banana', 70)
mydict.set('mango', 23)
print(mydict)
print(mydict.get('mango'))
print(mydict.keys())
print(mydict.values())
