class hashNode:
    
    # constructor
    def __init__(self, key, value):
        self.key = key
        self.value = value

class hashMap:
    
    # constructor
    def __init__(self):
        self.capacity = 20
        self.size = 0
        self.arr = [None] * self.capacity
        self.dummy = hashNode(-1, -1)

    # hash function
    def hashCode(self, key):
        return key % self.capacity

    # insert key-value pair
    def insertNode(self, key, value):
        temp = hashNode(key, value)
        hashIndex = self.hashCode(key)

        while self.arr[hashIndex] is not None and \
              self.arr[hashIndex].key != key and \
              self.arr[hashIndex].key != -1:
            hashIndex = (hashIndex + 1) % self.capacity

        if self.arr[hashIndex] is None or \
                    self.arr[hashIndex].key == -1:
            self.size += 1
        self.arr[hashIndex] = temp

    # delete by key
    def deleteNode(self, key):
        hashIndex = self.hashCode(key)

        while self.arr[hashIndex] is not None:
            if self.arr[hashIndex].key == key:
                temp = self.arr[hashIndex]
                self.arr[hashIndex] = self.dummy
                self.size -= 1
                return temp.value
            hashIndex = (hashIndex + 1) % self.capacity

        return -1

    # get value by key
    def get(self, key):
        hashIndex = self.hashCode(key)
        counter = 0

        while self.arr[hashIndex] is not None:
            if counter > self.capacity:
                return -1
            if self.arr[hashIndex].key == key:
                return self.arr[hashIndex].value
            hashIndex = (hashIndex + 1) % self.capacity
            counter += 1

        return -1

    # return map size
    def sizeofMap(self):
        return self.size

    # check if map is empty
    def isEmpty(self):
        return self.size == 0

    # display all key-value pairs
    def display(self):
        for node in self.arr:
            if node is not None and node.key != -1:
                print(f"display method: {node.key} {node.value}")

if __name__ == "__main__":
    h = hashMap()
    h.insertNode(1, 1)
    h.insertNode(2, 2)
    h.insertNode(2, 3)
    h.display()
    print(f'h.sizeofMap: {h.sizeofMap()}')
    print(f'h.deleteNode: {h.deleteNode(2)}')
    print(f'h.sizeofMap: {h.sizeofMap()}')
    print(f'h.isEmpty: {str(h.isEmpty()).lower()}')
    print(f'h.get: {h.get(2)}')