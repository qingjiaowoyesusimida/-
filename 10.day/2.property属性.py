class LaoWang(object):
	def __init__(self):
		self.money = 0
	@property
	def money(self):
		return self.__money
	@money.setter
	def money(self,value):
		if isinstance(value,int):
			self.__money = value
		else:
			print('error:不是整数型数字')
laowang = LaoWang
laowang.money = 100000000
print(laowang.money)
