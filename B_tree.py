import bisect

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
        
    def get_value(self, key):
        for index, key_ in enumerate(self.keys):
            if key_ == key:
                return self.values[index]
        return None

    def insert_entry(self, key, value):
        insert_index = self.get_insert_index(key)
        self.keys.insert(insert_index, key)
        self.values.insert(insert_index, value)
        return insert_index

    def split_no_parent(self):
        split_index = len(self)//2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        right_node = Node(
            self.keys[split_index+1:], 
            self.values[split_index+1:],
            self.children[split_index+1:]
        )
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        parent = Node([key_to_move_up],[value_to_move_up],[self, right_node])
        return parent

    def insert_child(self, insert_index, child):
        self.children.insert(insert_index, child)
        child.parent = self

    def split_with_parent(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        right_node = Node(
            self.keys[split_index+1:], 
            self.values[split_index+1:],
            self.children[split_index+1:]
        )
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        insert_index = self.parent.insert_entry(
            key_to_move_up, 
            value_to_move_up
        )
        self.parent.insert_child(insert_index+1, right_node)
        return self.parent

    def split(self):
        if self.parent is None:
            return self.split_no_parent()
        return self.split_with_parent()