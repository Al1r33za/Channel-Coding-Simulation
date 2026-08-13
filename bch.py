# BCH impelementaion:
import gf, crc
from lrsolve import berlekamp_massey
import lrsolve

# import numpy as np 

def encode(n, k, /, u, g):
	''' bch encoder (=crc encoder)'''
	return crc.encode(*(n,k), u =u, g =g)

def syndrome(n, k, t, /, r, field):
	''' calculate syndrome for binary bch.
	'''
	alph =field[0]
	a1 =alph[1]		# narrow sense ...

	S =[0]*2*t

	for i in range(2*t):
		S[i] =0
		mask =(1<<n)
		r_masked = r | mask
		for j in range(n):
			r_j = (r_masked >> (n-j-1)) & 1
			if r_j:
				aij = gf.power(a1, ((i+1)*j), field)
				S[i] ^= aij
			else:
				continue

	return S

def decode(n, k, t, /, r, field):
	''' decode bch code.
	'''
	loga =field[1]
	S   = syndrome(*(n, k, t), r, field)
	Sig = berlekamp_massey(S, field)
	Sig.reverse()

	err_loc = lrsolve.chien_search(Sig, field)
	mask = 1 << n
	r_masked = r | mask
	for ej in err_loc:
		r_masked ^= (1 << (n-loga[ej]-1))

	u_star = r_masked & ((1<<k)-1)
	return u_star, r_masked, S
