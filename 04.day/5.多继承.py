class A():
	def testA(self):
		print('------A------')
	def test(self):
		print('-----testA-----')
class B():
	def testB(self):
		print('----B------')
	def test(self):
		print('----testB----')
class C(A,B):
	pass
c = c()
c.tesA()
c.testB()
c.test()
print(c.__mro__)
