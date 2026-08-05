
from gf import *
import cir, poly
def encode(n, k, t, /, u:list, gen:list, field):
	pass
def encode_textbook(n, k, t, /, u :list, gen :list, field):
	''' Encode non-binary bch code with length 'n'.'''
	alph =field[0]
	loga =field[1]
	codeword = [0]*(n-k) + u
	leadg =n - k + 1		# >= 2t + 1
	leadc =0
	for i in range(k):
		if (u[-i] == 0):
			continue
		else:
			leadc = n - i
			break

	shift = leadc - leadg
	while (shift > 0):
		q = div(codeword(leadc),
		  		gen(leadg),
				field)
		pass
		

def syndrome(n, k, t, /, r :list, field) -> tuple:
	"""Calculate non-binary bch syndrome."""
	alph = field[0]
	loga = field[1]

	S    = [0] * (2*t)
	S1   = [0] * (n)
	for i, rr in enumerate(r):
		S1[i] = mul(rr, alph[i], field)
	
	for i in range(2*t):

		for ss in S1:
			S[i] ^= ss

		for j in range(n):
			S1[j] = mul(S1[j], alph[j], field)
		
	return S

f = exfield_gen(4, 0b11001)
# b = [f[0][0], f[0][5], f[0][10]]

# print(syndrome(15, 9, 2, r =[b[2], 0, b[1], b[2], 0, b[1], b[0]
# 							 , b[1], b[0], 0, 0, 0, 0, b[1], b[0]], field =f))

