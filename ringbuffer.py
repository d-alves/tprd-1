class RingBuffer:
	def __init__(self, size):
		self.data = [None for i in xrange(size)]
		self.size = size

	def addItem(self, item): #insere
		self.data.pop(0)
		self.data.append(item)

	def removeItem(self, i): #liberaEspacoPosicao
		self.data.pop(i)
		self.data.insert(i, None)

	def removeFirstItem(self):#liberaEspaco
		removeItem(0)

	def isEmpty(self):
		return self.data[0] == ""

	def hasSpace(self):
		return self.data[0] == None

	def firstItem(self):
		return self.data[0]

	def lastItem(self):
		return self.data[self.size - 1]

	def get(self):
		return self.data