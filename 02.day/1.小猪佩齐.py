class pig():
	def sleep(self):
		print('睡觉')
	def eat(self):
		print('吃东西')
	def intro(self):
		print('名字%s\n年龄%s\n颜色%s'%(self.name,self.age,self.color))
peiqi =pig()
peiqi.name = '佩齐'
peiqi.age = '12'
peiqi.color = '粉色'
peiqi.sleep()
peiqi.eat()
peiqi.intro()
qz = pig()
qz.name = '乔治'
qz.age ='10'
qz.color = '蓝色'
qz.sleep()
qz.eat()
qz.intro()
