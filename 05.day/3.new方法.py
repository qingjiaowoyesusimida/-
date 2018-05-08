class Dog(object):
	def __init__(self):
		print('init方法')
	def __str__(selfi):
		print('sstr股份')
		return '对象描述信息'
	def __del__(self):
		print('del方法')
	def __new__(cls):
		print('new方法')
		return object.__new__(cls)
dog = Dog()
print(id(dog))

