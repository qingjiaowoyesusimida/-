class SweetPotato():
	def __init__(self):
		self.cookedLever = 0
		self.cookedStr = '生的'
	def cook(self,time):
		self.cookedLever +=time
		if self.cookedLever >0 and self.cookedLever <4:
			self.cookedStr ='半生不熟'
		elif self.cookedLever >=4 and self.cookedLever<6:
			self.cookedStr ='烤好了'
		elif self.cookedLever >=6 and self.cookedLever<9:
			self.cookedStr='烤成炭了'
digua = SweetPotato
digua.cook(1)
jiyu.addliments('盐，酱油,芥末')
