class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def has_value(self, value):
		if self.data == value:
			return True
		return False