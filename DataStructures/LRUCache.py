class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.cache = {}
        self.size = 0

    def put(self, key, value):
        # do a normal insertion when a new key is being added to the cache and add it 
        # to the back of the queue indicating it was accessed recently
        if self.size < self.capacity and key not in self.cache:
            self.cache[key] = value
            # update the current size of the cache
            self.size +=1
            # update the position of the new item on the 
            # queue to indidcate it was accessed recently
            self.queue.append(key)

        # if the key is in the cache already, this means we want to update the value
        elif key in self.cache:
            self.cache[key] = value
            # update its position on the queue to indidcate it was accessed recently
            self.queue.remove(key)
            self.queue.append(key)

        # the cache is out of capacity so we need to remove the least
        #  accessed item and replace it with the new one     
        else:
            # delete the first item from the queue since
            leastaccessed = self.queue.pop(0)
            # delete if from the cache
            self.cache.__delitem__(leastaccessed)
            # add the new key, value pair to the cache
            self.cache[key] = value
            # add it to the back of the queue
            self.queue.append(key)

    def get(self, key):
        # if the key item is in the cache, update its position on the queue as recently 
        # accessed and return its value else return -1 if not in the cache
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache.get(key, -1)
