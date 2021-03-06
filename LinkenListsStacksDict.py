

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
    def __iter__(self):
        self._iter_node = self.head
        return self
    
    
    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        # Rest of the implementation goes here
        ret  = self._iter_node.data
        self._iter_node = self._iter_node.next
        return ret 

    def prepend(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def __len__(self):
        return self.length

    def __str__(self):
        return str([value for value in self])

####-------------------------------------------------------------------------------
####              QUEUE:
####-------------------------------------------------------------------------------

class Queue(LinkedList):
    
    def enqueue(self, data):
        self.prepend(data)
        
    def get_front(self):
        return self.tail.data
    
    def dequeue(self):
        ret = self.tail.data
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret

 ####-------------------------------------------------------------------------------
####              STACK:
####-------------------------------------------------------------------------------
#    
class Stack(LinkedList):
    
    def push(self, data):
        self.append(data)

    def peek(self):
        return self.tail.data

    def pop(self):
        ret = self.tail.data
        if self.length == 1:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret 