class Dog():
	name = '小黑'
	def run(self):
		print('吃吃')
	def move(self):
		print('跑跑跑')
	@classmethod
	def getCountry(cls):
		return cls.name
taidi =Dog()
taidi.run()
taidi.move()
print(Dog.getCountry())
print(taidi.getCountry())
