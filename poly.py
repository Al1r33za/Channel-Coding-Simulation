
from gf import *

def add(a :list, b :list, field):
	m =field[2]
	if (len(a) != len(b)):
		pass
	for i,ai in enumerate(a):
		b[i] ^= ai

	return b

def conv_mul(a :list, b :list, field) -> tuple:
	'''multiply polynomial a(x) by b(x)'''
	beta = field[0]
	m    = field[2]
	if (len(a) != len(b)):
		pass
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

	# r =r[:lenb-1]

	return q, r

def diff(a :list):
	for i in range(1, len(a), 2):
		a[i-1] =0
		a[i//2]=a[i]

	return a

# f16 = exfield_gen(4, 0b11001); al =f16[0]; loga =f16[1]
# a =[al[6], al[9], al[6], al[4], 
# 	al[14], al[10], al[0]]
# b =[al[0], al[3], al[10],
# 	al[10], al[4]]

# D =long_div(a, b, f16)
# Q =D[0]
# R =D[1]
# print(f'qutient :{[loga[i] for i in Q]}, \n remainder : {[loga[i] for i in R]}')

# a =[al[3], 0, 0, al[0], al[2]]
# b =[al[1], al[3]]

# d =long_div(a, b, f16)
# q =d[0]
# r =d[1]
# print(f'q: {[loga[i] for i in q]} \n r: {[loga[i] for i in r]}')