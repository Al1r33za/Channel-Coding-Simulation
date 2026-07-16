# algorithms for solving linear recursion

from gf import exfield_gen, mul, div
# m =4
# g =0b11001
# field =exfield_gen(m, g)
# alph  =field[0]

def berlekamp_massey(S, field):
	''' berlekamp_massey algorithm for constructing needed LFSR
	INPUTS:
	---------------------------
	S: list of int				/ input syndrome
	field: tuple of lists
	OUTPUTS:
	---------------------------
	Lambd: list of int			/ output error locator
	'''
	alph  =field[0]

	_2t =len(S)
	C =[0] * (_2t+1)
	B =[0] * (_2t+1)

	C[0] =alph[0]			# connection poly
	B[0] =alph[0]			# last connection poly
	L = 0               	# connection poly degree
	m = 1 					# m = mu - rho
	d =alph[0]; b = alph[0]	# current/last discrepancy

	for mu in range(_2t):

		# linear recursion
		d =S[mu]
		for i in range(1, L+1):
			d ^= mul(C[i], S[mu - i], field)


		if (d == 0):
			m +=1
		else:
			T = C.copy()
			A = div(d, b, field)

			# Connection poly modification
			for i in range(L + 1):
				C[i + m] ^= mul(A, B[i], field)

			if (2*L) <= mu:
				L = mu + 1 - L
				B = T
				b = d
				m = 1
			else:
				m += 1

	# res = [field[1][x] for x in C[:L+1]]
	return C[:L+1]
