class Per():
	def __init__(self):
		self.__money=100
	def germoney(self):
		return self.__money
	def sermoney(self,money):
		if money >= 0:
			self.__money = money
		else:
			print('输入的金额有误')
xiaoming = Per()
xiaoming.sermoney(10)
print(xiaoming.germoney())
		
