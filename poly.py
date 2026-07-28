
from gf import *

def add(a :list, b :list, field):
	

	beta = field[0]
	m    = field[2]

	for i,ai in enumerate(a):

		if (ai > (1 << m)) or (b[i] > (1 << m)):
			raise TypeError
		b[i] ^= ai

	return b

def mul(a :list, b :list, field):
	
	beta = field[0]
	m    = field[2]
	c = [0] *(len(a) + len(b) - 1)

	for i,ai in enumerate(a):
		for j,bj in enumerate(b):
			c[i+j] ^= mul(ai, bj, field)

	return c

def deriv(a :list, field):
	pass
