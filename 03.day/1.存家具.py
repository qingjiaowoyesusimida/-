class Home:
	def __init__(self,area,address,price):
		self.area = area
		self.address = address
		self.price = price
	def __str__(self):
		msg ='房子多少%d平\n房子在%s\n房子的价格%s'%(self.area,self.address,self.price)
		return msg
class Bed:
	def __init__(self,area,name,price):
		self.area=area
		self.name=name
		self.price=price
	def __str__(self):
		mag ='床的面积为%d平\n床的品牌%s\n床的价格%s'%(self.area,self.name,self.price)
		return mag
myhome = Home(220,'朝阳区','1500万')
print(myhome)
mybed = Bed(20,'席梦思','4万')
print(mybed)
