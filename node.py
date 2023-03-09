class DLLNode:
    def __init__(self, new_data):
        self.data = new_data
        self.prev_node = None
        self.next_node = None

    def insert_after (self, other_node):
        if self.next_node is not None:
            aux_node = self.next_node
            aux_node.prev_node = other_node
            other_node.next_node = aux_node

        self.next_node = other_node
        other_node.prev_node = self

        return self
    
    def insert_before (self, other_node):
        if self.prev_node is not None:
            aux_node = self.prev_node
            aux_node.next_node = other_node
            other_node.prev_node = aux_node
            
        self.prev_node = other_node
        other_node.next_node = self

        return self
    
    def remove_before(self):
        if self.prev_node is None:
            raise ValueError("No hay un nodo previo que eliminar.")
        else:
            self.prev_node.prev_node.next_node = self
            self.prev_node = self.prev_node.prev_node       

    def remove_after(self):
        if self.next_node is None:
            raise ValueError("No hay un siguiente nodo que eliminar.")
        else:
            self.next_node.next_node.prev_node = self
            self.next_node = self.next_node.next_node
