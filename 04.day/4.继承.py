class Father(object):
	def __init__(self):
		self.__girl_count = 4
	def getweight(self):
		return self.__girl_count
	def money(self):
		print('会挣钱')
	def Run(self):
		print('跑步')
	def __obj(self):
		print('处对象')
	def setspeak(self):
		self.__obj()
class Per(Father):
	pass
xiaoming = Per()
xiaoming.money()
xiaoming.Run()
print(xiaoming.getweight())
xiaoming.setspeak()
