class Node:
    
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0

    def contains_key(self, key):
        return key in self.keys
        