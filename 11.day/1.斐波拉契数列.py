def fid(times):
	n = 0
	a,b = 0,1
	while n<times:
		yield b
		a,b = b,a+b
		n+=1
F = fid(5)
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
