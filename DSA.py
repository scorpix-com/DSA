class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash_value(self, key):
        h = 0
        for data in key:
            h += ord(data)
        
        return h%10

    def __setitem__(self, key, value):
        h = self.get_hash_value(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash_value(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash_value(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
        


ht = HashTable()
print(ht.get_hash_value("march 9"))
ht["march 6"] = 120
ht["march 17"] = 345
ht["march 2"] = 270
ht["december 10"] = 156

print(ht["march 6"])
print(ht.arr)

del ht["march 6"]
del ht["december 10"]

print(ht.arr)