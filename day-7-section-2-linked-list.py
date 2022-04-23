class Node:
  def __init__(self, data, reference=None):
    self.data = data
    self.reference = reference
  def add_to_start(self, data):
    n_node = Node(data)
    n_node.reference = self.head
    self.head= n_node


class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def printed_linked_list(self):
    if self.head is None:
      print("The Linked list is empty")
    else:
      c_node = self.head
      while c_node is not None:
        print(c_node.data)
        c_node = c_node.reference
  

linked_list1 = LinkedList()
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)
linked_list1.print_linked_list()

    
node1 = Node(5)
print(node1.data)

node2 = Node(11)
node1.reference = node2
print(node1.reference)