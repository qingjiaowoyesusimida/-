class Boy():
	def __init__(self,name,age,height,weight):
		self.name = name
		self.age = age
		self.height=height
		self.weight=weight
		self.address = '沈阳'
		self.games = []
	def study(self):
		print('学习')
	def open_car(self,car):
		print('开车%s'%car)
	def showage(self):
		print('年龄是%d'%self.age)
	def addgames(self,game):
		for i in self.games:
			print(i)
lx = Boy('李鑫',18,175,120)
lx.study()
lx.open_car('奔驰G560')
lx.showage()

