import sys


def contfrac_div (x, y):
	'''Return the ratio of two positive ints as a continued fraction.'''
	a = x/y
	if a * y == x:
		return [a]
	else:
		list = contfrac_div(y, x - a * y)
		list.insert(0, a)
		return list
