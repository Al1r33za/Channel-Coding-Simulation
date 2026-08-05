
from gf import *
import cir, poly
def encode(n, k, t, /, u:list, gen:list, field):
	''' Encode non-binary bch code with length 'n'.
	
	Key Arguments:
	n --
	k --
	t -- 
	u -- information src
	gen -- generator polynomial
	field -- q-ary field'''
	alph, loga =field[0], field[1]
	regs =[0]*(len(gen) -1)
	for clk in range(len(u) + len(gen) - 1):
		regs[0] = u[-(clk + 1)]

		for i in range(len(regs)):
			if (regs[-1] ==0):
				regs[i] = regs[i-1]
			else:
				regs[i] ^= mul(regs[i-1], gen[i], field)

	return regs

def encode_textbook(n, k, t, /, u :list, gen :list, field):
	''' Encode non-binary bch code with length 'n'.
	
	Notes: this is textbook encoder which is a systematic encoder (uses long devision).'''
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

f16 = exfield_gen(4, 0b11001)
# b = [f[0][0], f[0][5], f[0][10]]

# print(syndrome(15, 9, 2, r =[b[2], 0, b[1], b[2], 0, b[1], b[0]
# 							 , b[1], b[0], 0, 0, 0, 0, b[1], b[0]], field =f))

