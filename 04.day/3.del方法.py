class Pen():
	def __del__(self):
		print('大刀瑞雯')
lix = Pen()
lix2 = lix
del lix
del lix2
print('结束')
