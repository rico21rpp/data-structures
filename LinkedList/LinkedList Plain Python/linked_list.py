# method documentation by https://www.theodinproject.com/courses/ruby-programming/lessons/linked-lists
from node import Node

class LinkedList:
	def __init__(self, head = None):
		self.head = head
		self.tail = head

	def is_empty(self):
		return self.head == None

	def instantiate_node_when_needed(self, item):
		if not isinstance(item, Node):
			item = Node(item)
		return item

	#adds a new node containing value to the end of the list
	def append(self, item):
		item = self.instantiate_node_when_needed(item)
		if self.is_empty():
			self.head = item
			self.tail = item
		elif self.head == self.tail:
			self.tail = item
			self.head.next = item
		else:
			self.tail.next = item
			self.tail = item

	#prepend(value) adds a new node containing value to the start of the list

	#size returns the total number of nodes in the list

	#at(index) returns the node at the given index

	#pop removes the last element from the list

	#contains?(value) returns true if the passed in value is in the list and otherwise returns false

	#isEmpty

	#find(value) returns the index of the node containing value, or nil if not found

	#to_s represent your LinkedList objects as strings, so you can print them out and preview them in the console. The format should be: ( value ) -> ( value ) -> ( value ) -> nil

	#insert_at(value, index) that inserts the node with the provided value at the given index

	#remove_at(index) that removes the node at the given index. (You will need to update the links of your nodes in the list when you remove a node.) </div>