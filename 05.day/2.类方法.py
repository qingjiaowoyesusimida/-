class DateTest():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def outDate(self):
		print('%s年%s月%s日'%(self.year,self.month,self.day))
	@classmethod
	def handleDate(cla,date):
		a,b,c = date.split('-')
		d = cls(a,b,c)
		return d
#a = 2018
#b = '05'
#c = '04'
#d = DateTest(a,b,c)
#d.outDate()
str = '2019-06-07'
a,b,c = str.split('-')
d = DateTest(a,b,c)
d.outDate()

