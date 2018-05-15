def line_conf(a,b,c):
	def line(x,y):
		return a*x+b*c+y
	return line
line1 = line_conf(1,1,2)
line2 = line_conf(4,5,3)
print(line1(5,2))
print(line2(5,2))
