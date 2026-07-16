# BCH impelementaion:
import gf, cir, crc
from lrsolve import berlekamp_massey

# import numpy as np 

alph =gf.exfield_gen(4, 0b11001)

def encode(n, k, /, u, g):
	''' bch encoder (=crc encoder)'''
	return crc.encode(*(n,k), u =u, g =g)

def syndrome(n, k, /, r, t =3):
	''' syndrome calculation for bch(n,k,t)
	(n, k): int, int 		/ information/codewrod length
	r: 		int 			/ received polynomial
	g:		int 			/ minimal generator
	'''
	S =[0] *(2*t)

	for i in range(2*t):
		beta =alph[i+1]
		si = 0
		rr =r
		for _ in range(n):
			rn, rr =cir.bit_pop(rr)
			
			si =gf.mul(4, si, beta)
			if rn:
				si ^= 1
		S[i] =si
	return S

def decode(n, k, t, /, r, g, m):
	'''
	'''
	gf2m= gf.exfield_gen(m, g)
	S   = syndrome(*(n, k), r, t)
	Sig = berlekamp_massey(S, gf2m)
	pass
