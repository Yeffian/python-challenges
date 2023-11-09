class HashTable:
    def __init__(self) -> None:
        self.keys = []
        self.values = []

    def put(self, key, value):
        self.keys.append(key)
        self.values.append(value)
    
    def delete(self, key):
        index = self.keys.index(key)
        self.keys.pop(index)
        self.values.pop(index)
    
    def get(self, key):
        index = self.keys.index(key)
        return self.values[index]
    

table = HashTable()
table.put("One", 1)
table.put("Two", 2)
print(table.get("One"))
