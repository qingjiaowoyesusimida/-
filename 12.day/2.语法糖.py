def w1(fun):
	def inner():
		print('验证')
		fun()
	return inner
@w1
def test():
	print('验证成功')
test()
