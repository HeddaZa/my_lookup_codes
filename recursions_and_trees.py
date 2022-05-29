### print all files in directory and subdirectories
import os

def list_files(current_path):
    if not os.path.isdir(current_path):
        print(current_path)
    else:
        for name in os.listdir(current_path):
            joined = os.path.join(current_path, name)
            list_files(joined)
list_files('folder')

#####-------------------------------------------------------
#### Binary Tree: sorting

class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    
    def __init__(self):
        self.root = None
        
    def add(self, value):
        if self.root is None:
            # The root does exist yet, create it
            self.root = Node(value)
        else:
            # Find the right place and insert new value
            self._add_recursive(self.root, value)
            
    def _add_recursive(self, current_node, value):
        if value <= current_node.value:
            # Go to the left, add value if there is no node, otherwise: recursion
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            # Go to the right, add value id there is no node, otherwise: recursion
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)

    def _contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)
    
    def contains(self, value):
        return self._contains(self.root, value)
                