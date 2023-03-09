from double_linked_list import DLLNode

class DLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.size = 0
    
    def add(self, new_data):
        node = DLLNode(new_data)
        if self.first_node is None:
            self.first_node = node
            self.last_node = node
        else:
            self.last_node.insert_after(node)
            self.last_node = node
        self.size += 1

    def get_size(self):
        return self.size
    
    def get(self, position):
        node = self.first_node

        if position < 0 or position >= self.size:
            raise ValueError(f"El índice es inválido ({position}).")
        
        if position == self.size - 1:
            return self.last_node
        else:
            for i in range(position):
                node = node.next_node
            return node

    def insert_at(self, position, new_data):
        node = DLLNode(new_data)

        if position < 0 or position >= self.size:
            raise ValueError(f"El índice es inválido ({position}).")
        else:
            current_node = self.get(position)
            current_node.insert_before(node)
        
        if position == 0:
            self.first_node = node

        self.size += 1

    def remove_at(self, position):
        if position < 0 or position >= self.size:
            raise ValueError(f"El índice es inválido ({position}).")
        
        if self.first_node is None:
            raise ValueError("La lista está vacia.")

        if position == 0:
            self.first_node.next_node.prev_node = None
            self.first_node = self.first_node.next_node
        elif position == self.size - 1:
            self.last_node.prev_node.next_node = None
            self.last_node = self.last_node.prev_node
        else:
            node = self.get(position)

            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node

        self.size -=1
