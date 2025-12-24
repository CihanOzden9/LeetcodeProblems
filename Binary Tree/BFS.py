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
            # Eğer yeni eklenen node mevcutsa ağaçta False döndür
            if new_node.value == temp_node.value:
                return False
            
            #yeni Node kökten küçükse
            if new_node.value < temp_node.value:
                #Kökün solu boş ise sola ekle
                if temp_node.left is None:
                    temp_node.left = new_node
                    return True
                temp_node = temp_node.left

            #Büyükse aynı kuralları uygula
            else:
                if temp_node.right is None:
                    temp_node.right = temp_node
                    return True
                temp_node = temp_node.right
    
    
    def contains(self, value):
        temp_node = self.root
        while True:
            if value < temp_node.value:
                temp_node = temp_node.left

            elif value > temp_node.value:
                temp_node = temp_node.right
            
            else:
                return True
        return False
    
    def min_of_node(self, curr):
        while curr.left:
            curr = curr.left
        return curr
    
    def max_of_node(self, curr):
        while curr.right:
            curr = curr.right
        return curr