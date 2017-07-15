class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def adelantar_elemento_N(self,N):
		if self.isEmpty not False:
			while N not 1:
				elemento=self.dequeue
				self.enqueue(a)
		else:
			return True
