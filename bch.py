# BCH impelementaion:
import gf, cir, crc
from lrsolve import berlekamp_massey
import lrsolve

# import numpy as np 

def encode(n, k, /, u, g):
	''' bch encoder (=crc encoder)'''
	return crc.encode(*(n,k), u =u, g =g)

def syndrome(n, k, t, /, r, field):
	''' syndrome calculation for bch(n,k,t)
	(n, k): int, int 		/ information/codewrod length
	r: 		int 			/ received polynomial
	g:		int 			/ minimal generator
	'''
	alph =field[0]
	expo =field[1]

	S =[0] *(2*t)

	for i in range(2*t):
		beta =alph[i+1]
		S[i] =0

		for j in range(n):

			if (r >> (n-1-j)) & 1:
				S[i] ^= gf.power(beta, j, field)

	return S

def decode(n, k, t, /, r, field):
	'''
	'''
	S   = syndrome(*(n, k, t), r, field)
	Sig = berlekamp_massey(S, field)
	Sig.reverse()
	err_loc = lrsolve.chien_search(Sig, field)

	print(f'error locations: {err_loc}')
	for ej in err_loc:
		r ^= (1 << (n-1-ej))
	return r

C =(15, 5, 3); field =gf.exfield_gen(4, 0b11001); a =field[0]
# 
# assert syndrome(*C, r =0b000_101_000_000_100, field =field) == [a[0], a[0], a[10], a[0], a[10], a[5]]
# assert decode(*(15, 5, 3), r =0b000_101_000_000_100, field =field) == 0

print(syndrome(*C, r =0b011000001, field =field))
print(syndrome(*C, r =0b111000001, field =field))