def printfunction(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

def poly(x):
	return 2 * x**2 - 4 * x + 2

printfunction([x for x in range(-2, 3)], poly)

#
def printfunction(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

printfunction([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)