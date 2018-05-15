def w1(fun):
	def inner():
		print('验证')
		fun()
	return inner
def test():
	print('验证成功')
test = w1(test)
test()
