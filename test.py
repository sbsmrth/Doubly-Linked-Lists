from node import DLLNode
from list import DLinkedList

def print_node(node):
    print("Node [Address:" , id(node) , "]")
    print("- Data:" , (node.data))
    if node.prev_node is not None:
        print("- Prev node: [Address:" , id(node.prev_node) , "]")
    else:
        print("- Prev node: [Address: None]")
    if node.next_node is not None:
        print("- Next node: [Address:" , id(node.next_node) , "]")
    else:
        print("- Next node: [Address: None]")
    print("\n")

node1 = DLLNode(390)
node2 = DLLNode(470)
node3 = DLLNode(510)
node4 = DLLNode(901)
node5 = DLLNode(888)

node1.insert_after(node2)
node1.insert_after(node3)
node1.insert_before(node4)

print_node(node1)
print_node(node2)
print_node(node3)
print_node(node4)

node_temp = node1

while node_temp.prev_node is not None:
    node_temp = node_temp.prev_node

print("Print all nodes from the first node to the last.")
print_node(node_temp)

while node_temp.next_node is not None:
    node_temp = node_temp.next_node
    print_node(node_temp)

print("Print all nodes from the last to the first.")
print_node(node_temp)

while node_temp.prev_node is not None:
    node_temp = node_temp.prev_node
    print_node(node_temp)


list = DLinkedList()
list.add(35)
list.add(50)
list.add(100)
list.add(236)

print("List Section:")

print_node(f"First node: {list.get(1)}")

list.insert_at(0,9)
list.insert_at(4, 12)
list.remove_at(3)
