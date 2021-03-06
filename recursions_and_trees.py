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

######-------------------------------------------------------------------------------------
#### AVL tree with Node class:

class AVLNode(Node):
    
    def __init__(self, value):
        super().__init__(value)
        self.height = 1
        self.imbalance = 0
        
    def calculate_height_and_imbalance(self):
        if self.left_child is None:
            left_height = 0
        else:
            left_height = self.left_child.height
        if self.right_child is None:
            right_height = 0
        else:
            right_height = self.right_child.height
        self.height = 1 + max(left_height, right_height)
        self.imbalance = left_height - right_height

class AVLTree(BST):
    
    def __init__(self):
        super().__init__()
        
    def _add_recursive(self, current_node, value):
        if current_node is None:
            return AVLNode(value)
        if value <= current_node.value:
            current_node.left_child = self._add_recursive(current_node.left_child, value)
        else:
            current_node.right_child = self._add_recursive(current_node.right_child, value)
        current_node.calculate_height_and_imbalance() 
        if abs(current_node.imbalance) == 2:
            return self._balance(current_node)  
        return current_node

    def get_height(self):
        return self.root.height
    
    def _rotate_left(self, node):
        pivot = node.right_child
        node.right_child = pivot.left_child
        pivot.left_child = node
        node.calculate_height_and_imbalance()
        pivot.calculate_height_and_imbalance()
        return pivot
    
    def _rotate_right(self, node):
        pivot = node.left_child
        node.left_child = pivot.right_child
        pivot.right_child = node
        node.calculate_height_and_imbalance()
        pivot.calculate_height_and_imbalance()
        return pivot

    def _balance(self, node):
        if node.imbalance == 2:
            pivot = node.left_child
            if pivot.imbalance == 1:
                return self._rotate_right(node)
            else:
                node.left_child = self._rotate_left(pivot)
                return self._rotate_right(node)
        else:
            pivot = node.right_child
            if pivot.imbalance == -1:
                return self._rotate_left(node)
            else:
                node.right_child = self._rotate_right(pivot)
                return self._rotate_left(node)

#####-------------------------------------------------------------------------------
#### HEAP TREE: min-heap
class MinHeap:
    
    def __init__(self):
        self.values = []
        
    def _left_child(self, node):
        return 2 * node + 1

    def _right_child(self, node):
        return 2 * node + 2
    
    def _parent(self, node):
        return (node - 1) // 2

    def _swap(self, node1, node2):
        tmp = self.values[node1]
        self.values[node1] = self.values[node2]
        self.values[node2] = tmp

    def add(self, value):
        self.values.append(value)
        self._heapify_up(len(self.values) - 1)
    
    def _heapify_up(self, node):
        parent = self._parent(node)
        if node > 0 and self.values[parent] > self.values[node]:
            self._swap(node, parent)
            self._heapify_up(parent)
            
    def min_value(self):
        return self.values[0]
    
    def pop(self):
        self._swap(0, len(self.values) - 1)
        ret_value = self.values.pop()
        self._heapify_down(0)
        return ret_value

    def _heapify_down(self, node):
        left_child = self._left_child(node)
        right_child = self._right_child(node)
        if left_child < len(self.values): 
            if right_child < len(self.values):
                min_node = min(left_child.values, right_child.values)
            else:
                min_node = left_child.values
        elif right_child < len(self.values):
            min_node = right_child.values
        if min_node:
            self._swap(node, min_node)
            self._heapify_down(min_node)
                