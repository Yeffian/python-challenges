class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
    
    def len(self):
        result = 0
        current = self.head
        while current.next is not None:
            result += 1
            current = current.next
        
        return result

    def append(self, data):
        new = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new

    def delete(self, i):
        idx = 0
        if i >= self.len():
            raise IndexError()
        
        current = self.head
        while True:
            prev = current
            current = current.next
            if idx == i:
                prev.next = current.next
                return
            else:
                idx += 1

    def get(self, i):
        idx = 0
        if i >= self.len():
            raise IndexError()

        current = self.head
        while current.next is not None:
            current = current.next
            if idx == i:
                return current.data
            else:
                idx += 1
    
    def __repr__(self) -> str:
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
            elements.append(current.data)
        
        return str(elements)
    

ll = LinkedList()
ll.append("A")
ll.append("B")
print(ll)
print(ll.get(0))
ll.delete(0)
print(ll)