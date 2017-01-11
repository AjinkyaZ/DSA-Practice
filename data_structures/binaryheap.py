# Binary Heap 
# allows enqueue and dequeue in O(logn)
# MinHeap implementation

class BinaryHeap:
	def __init__(self):
		self.heapList = [0]
		self.size = 0

	def percolateUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				temp = self.heapList[i // 2]
				self.heapList[ i // 2] = self.heapList[i]
				self.heapList[i] = temp
			i = i // 2

	def insert(self, item):
		self.heapList.append(item)
		self.size = self.size + 1
		self.percolateUp(self.size)

#to-do, incomplete