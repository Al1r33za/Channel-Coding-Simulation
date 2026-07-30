
from gf import *

def encode(n, k, t, /, u, field):
	''' Encode non-binary bch code with length 'n'.'''
	pass

def syndrome(n, k, t, /, r :list, field) -> tuple:
	"""Calculate non-binary bch syndrome."""
	alph = field[0]
	loga = field[1]
	m    = field[2]

	S    = [0] * (2*t)
	S1   = 0
	for i, rr in enumerate(r):
		if (i == 0):
			continue
		S1 ^= mul(rr, alph[i], field)
	S[0] = loga[S1 ^ r[0]]
	for i in range(1, 2*t):
		S1 = mul(alph[i], S1, field)
		S[i] = loga[S1 ^ r[0]]
	
	return tuple(S)

f = exfield_gen(4, 0b11001)
b = [f[0][0], f[0][5], f[0][10]]

print(syndrome(15, 9, 2, r =[b[2], 0, b[1], b[2], 0, b[1], b[0], b[1], b[0], 0, 0, 0, 0, b[1], b[0]], field =f))

