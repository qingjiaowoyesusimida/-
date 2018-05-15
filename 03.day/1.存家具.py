class Home:
	def __init__(self,area,address,price):
		self.area = area
		self.address = address
		self.price = price
	def __str__(self):
		msg ='房子多少%d平\n房子在%s\n房子的价格%s'%(self.area,self.address,self.price)
		return msg
	def addBed(self,bed):
		if self.area >= bed.getArea():
			self.jiaju.append(bed)
			self.area -= bed.getArea()
			print('加入成功')
			print(self.area)
		else:
			print('加入失败')
	def addLight(self,light):
		self.dengs.append(light)
	def switch(self):
		if self.dengs[0].getIsopen():
			self.dengs[0].close()
		else:
			self.dengs[0].open()
class Bed:
	def __init__(self,area,name,price):
		self.area=area
		self.name=name
		self.price=price
	def __str__(self):
		mag ='床的面积为%d平\n床的品牌%s\n床的价格%s'%(self.area,self.name,self.price)
		return mag
	def getArea(self):
		return self.area
class Light():
	def __init__(self,name):
		self.name = name
		self.isopen = False
	def __str__(self):
		msg = '我叫%s灯'%self.name
		return msg
	def open(self):
		self.isopen = True
		print('灯亮了')
	def close(self):
		self.isopen = False
		print('灯灭了')
	def getIsopen(self):
		return self.isopen
myhome = Home(220,'朝阳区','1500万')
print(myhome)
mybed = Bed(20,'席梦思','4万')
print(mybed)
benladeng = Light('本拉登')
print(benladeng)
myhome.appLight(denladeng)
for i in range(10):
	myhome.switch()
myhome.addBed(ximengsi)
myhome.addBed(ximengsi)
myhome.addBed(ximengsi)
myhome.addBed(ximengsi)
myhome.addBed(ximengsi)
myhome.addBed(ximengsi)
myhome.addBed(ximengsi)
