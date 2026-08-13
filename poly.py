
from gf import *

def add(a :list, b :list, field):
	m =field[2]
	if (len(a) != len(b)):
		pass
	for i,ai in enumerate(a):
		b[i] ^= ai

	return b

def conv(a :list, b :list, field) -> tuple:
	'''multiply polynomial a(x) by b(x)'''

	c = [0] *(len(a) + len(b) - 1)

	for i,ai in enumerate(a):
		for j,bj in enumerate(b):
			c[i+j] ^= mul(ai, bj, field)

	return c

def shift_scale(a :list, shift :int, scale :int, field):
	pass

def long_div(a :list, b :list, field) -> tuple:
	'''Divide polynomial a(x) by b(x). 
	
	Long division ...'''
	alph =field[0]
	loga =field[1]
	lenb =len(b)
	lena =len(a)
	q = [0]*(lena - lenb + 1)
	r = a[:]
	for lead in range(1, lena - lenb +2):
		q[-lead] = div(r[-lead], b[-1], field)
		
		for i in range(lenb):
			r[-lead-i] ^= mul(b[-i-1], q[-lead], field)

	r =r[:lenb-1]
	return q, r

def diff(a :list):
	a =a.copy()
	if (len(a) %2):
		a.pop()

	a[0::2] = a[1::2]
	a[1::2] = [0] * (len(a)//2)
	a.pop()
	return a

def eval(a :list, x :int, field):
	'''Evaluate polynomial a(x) at x.'''
	alph =field[0]
	loga =field[1]
	y =0
	for ai in reversed(a):
		y = mul(y, x, field) ^ ai

	return y
