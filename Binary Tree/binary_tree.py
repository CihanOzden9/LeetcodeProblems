class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        temp_node = self.root

        while True:
            if new_node.value == temp_node.value:
                return False
            
            if new_node.value < temp_node.value:
                if temp_node.left is None:
                    temp_node.left = new_node
                    return True
                temp_node = temp_node.left
            
            else:
                if temp_node.right is None:
                    temp_node.right = temp_node
                    return True
                temp_node = temp_node.right