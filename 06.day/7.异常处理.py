class Test(object):
	def __init__(self,switch):
		self.switch = switch
	def calc(self,a,b):
		try:
			return a/b
		except Exception as result:
			if self.switch:
				print('捕捉到异常')
				print(result)
			else:
				raise
a = Test(True)
a.calc(11,0)
print('----------华丽的分割线---------')
a.switch = False
a.calc(11,0)
