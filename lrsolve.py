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
			m += 1
		else:
			T = C.copy()
			A = div(d, b, field)

			# Connection poly modification
			for i in range(L + 1):
				C[i + m] ^= mul(A, B[i], field)		# correction term: A.X^m.B_i

			if (2*L) <= mu:
				L = mu + 1 - L
				B = T
				b = d
				m = 1
			else:
				m += 1

	# res = [field[1][x] for x in C[:L+1]]
	return C[:L+1]

def berlekamp_massey_binary(S, field):
	pass

def Euclidean(a, b, field):
	'''Euclidean algortihm.

	Key Argument:
	a -- polynomial
	b -- polynomial
	field -- field elements
	'''
	
	pass
def chien_search(L :list, field):
	'''
	'''

	alph =field[0]
	expo =field[1]
	m    =field[2]
	n =(1 << m) - 1
	l =len(L)
	roots=[]

	for j in range(n):

		beta =alph[j]
		Lj = 0
		ax =alph[0]

		for lami in L:
			Lj ^=mul(lami, ax, field)
			ax =mul(ax, beta, field)

		if (Lj == 0):
			roots.append(expo[beta])

	return roots

# field =exfield_gen(4, 0b11001); a =field[0]
# S =[a[0], a[0], a[10], a[0], a[10], a[5]]
# L =[a[5], 0, a[0], a[0]]

# assert [a[0], a[0], 0, a[5]] == berlekamp_massey(S, field)
# assert [3, 5, 12] == chien_search(L, field)