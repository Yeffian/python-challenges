class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
    
    def is_empty(self):
        return self.length == 0

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            
            last.next = node
        
        self.length += 1

    def remove(self):
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value
    
class OptimizedQueue:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.last = None
    
    def is_empty(self):
        return self.length == 0
    
    def insert(self, value):
        node = Node(value)

        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node

        self.length += 1

    def remove(self):
        value = self.head.value
        self.head = self.head.next

        self.length -= 1
        if self.length == 0:
            self.last = None

        return value
    
class PriorityQueue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return not self.items
    
    def insert(self, item):
        self.items.append(item)
    
    def remove(self):
        maxi = 0

        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
                
        item = self.items[maxi]
        del self.items[maxi]
        return item
        
class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)
    
    def __gt__(self, other):
        return self.score < other.score
    

tiger = Golfer("Tiger Woods", 61)
hal = Golfer("Hal Sutton", 69)
phil = Golfer("Phil Mickelson", 72)

pq = PriorityQueue()

pq.insert(tiger)
pq.insert(hal)
pq.insert(phil)

while not pq.is_empty():
    print(pq.remove())