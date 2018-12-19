class Node: 
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		curr_node = self.head
		while curr_node:
			print(curr_node.data)
			curr_node = curr_node.next

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def swap(self, key1, key2):
		node_1, node_2 = self.head, self.head
		prev_1, prev_2 = None, None
		while node_1 and node_1.data != key1:
			prev_1 = node_1
			node_1 = node_1.next
		while node_2 and node_2.data != key2:
			prev_2 = node_2
			node_2 = node_2.next
		if node_1 is None or node_2 is None:
			return 

		prev_1.next = node_2
		prev_2.next = node_1


obj = LinkedList()
obj.append("A")
obj.append("B")
obj.append("C")
obj.append("D")
obj.append("E")
obj.swap("B", "D")
obj.print_list()