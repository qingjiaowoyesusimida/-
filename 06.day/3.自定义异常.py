class ShowError(Exception):
	def __init__(self,lenght,atleast):
		self.length = length
		self.atlenast = atlenast
def main():
	try:
		s = input('请输入')
		if len(s)<3:
			raise ShowError(len(3),3)
	except ShowEorror as result:
		print('showError:输入的长度是%d,长度至少是%d'%(result.length,length,result.atleast))
	else:
		print('没有异常')
main()
