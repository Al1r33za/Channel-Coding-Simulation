# algorithms for solving linear recursion

from gf import exfield_gen, mul, div
import poly
# m =4
# g =0b11001
# field =exfield_gen(m, g)
# alph  =field[0]

def berlekamp_massey(S :list, field):
	''' Find error locator polynomial (sigma).
	'''
	alph  =field[0]

	t =len(S)//2
	C =[0] * (2*t+1)
	B =[0] * (2*t+1)

	C[0] =alph[0]			# connection poly
	B[0] =alph[0]			# last connection poly
	L = 0               	# connection poly degree L = len(B)
	shift = 1 				# shift = mu - rho
	d =alph[0]; b = alph[0]	# current/last discrepancy

	for mu in range(2*t):

		# compute discrepancy
		d =S[mu]
		for i in range(1, L+1):
			d ^= mul(C[i], S[mu - i], field)

		if (d == 0):
			shift += 1
		else:
			T = C.copy()
			A = div(d, b, field)

			# Connection poly modification
			for i in range(L + 1):
				C[i + shift] ^= mul(A, B[i], field)		# correction term: A.X^m.B_i

			if (2*L) <= mu:
				L = mu + 1 - L
				B = T
				b = d
				shift = 1
			else:
				shift += 1

	# res = [field[1][x] for x in C[:L+1]]
	return C[:L+1]

def BM(S :list, field):
	''' Find error locator polynomial (sigma).
	'''
	alph  =field[0]

	t =len(S)//2
	C =[0] * (2*t+1)
	B =[0] * (2*t+1)

	C[0] =alph[0]			# connection poly
	B[0] =alph[0]			# last connection poly
	L = 0               	# connection poly degree L = len(B)
	shift = 1 				# shift = mu - rho
	d =alph[0]; b = alph[0]	# current/last discrepancy

	for mu in range(2*t):

		# compute discrepancy
		d =S[mu]
		for i in range(1, L+1):
			d ^= mul(C[i], S[mu - i], field)

		if (d == 0):
			shift += 1
		else:
			T = C.copy()
			A = div(d, b, field)

			# Connection polynomial modification
			for i in range(L + 1):
				C[i + shift] ^= mul(A, B[i], field)		# correction term: A.X^m.B_i

			if (2*L) <= mu:
				L = mu + 1 - L
				B = T
				b = d
				shift = 1
			else:
				shift += 1

	# res = [field[1][x] for x in C[:L+1]]
	Z = poly.conv(S, C, field)
	Z = Z[:len(S)]

	return C, Z

def chien_search(L :list, field):
	'''Search for roots of the locator polynomial L.

	Returns the actual field elements that make the polynomial vanish, not their
	exponent tags. That is what the higher-level RS decoder expects for the
	Forney evaluator and location conversion in `rs.decode`.
	'''
	alph = field[0]
	loga = field[1]
	m    = field[2]
	n = (1 << m) - 1
	roots = []

	for i in range(n):
		beta = alph[i]
		ai = alph[0]
		Lai = 0
		
		for ll in L:
			Lai^= mul(ll,   ai, field)
			ai  = mul(ai, beta, field)

		if Lai == 0:
			roots.append(beta)

	return roots

def Euclidean(S :list, field):
	'''Euclidean algortihm.

	Key Argument:
	S(X) -- polynomial 
	field -- field elements
	'''
	alph =field[0]
	X2t = [0]*(len(S))
	X2t.append(alph[0])

	q1, r1 =poly.long_div(X2t, S, field)
	#
	# Update ... 
	# The complextity of this function is O(n^3) so im not gonna use it!
	pass


# f16 =exfield_gen(4, 0b11001); a =f16[0]
# S =[a[0], a[0], a[10], a[0], a[10], a[5]]
# L =[a[5], 0, a[0], a[0]]

# assert [a[0], a[0], 0, a[5]] == berlekamp_massey(S, f16)
# assert [3, 5, 12] == chien_search(L, f16)