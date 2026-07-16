# tools for making finite Galois field:
# import time

# class xfield:
# 	def __init__(self, m, g):
# 		self.m =m
# 		self.exp, self.log =exfield_gen(m, g)
# 		self.zro  =0
# 		self.one  =1

# 	def add(self, a, b):
# 		return add(self.m, a, b)

# 	def mul(self, a, b):
# 		return mul(self.m, a, b, self.exp)
		
# 	def inv(self, a):
# 		if a ==0:
# 			raise ZeroDivisionError
# 		return div(self.m, 1, a, self.exp)

# def add(m :int, a, b):
# 	''' xor in extended field '''
# 	n = 2**m
# 	if bool((a | b) >> m):
# 		a %= n-1
# 		b %= n-1

# 	return a ^ b

def mul(m :int, a :int, b :int, v :int) -> int:
	''' multiplication in extended field '''
	n = 2**m
	if bool((a | b) >> m):
		a %= n-1
		b %= n-1
	if (a == 0 or b == 0):
		return 0;
	
	i =v[1][a]
	j =v[1][b]
	xk = v[0][(i+j) % n-1]
	return xk

def div(m :int, a, b, v):
	''' division in extended field '''
	n = 2**m
	if bool((a | b) >> m):
		a %= n-1
		b %= n-1

	i =v[1][a]
	j =v[1][b]
	xk = v[0][(i-j) % n-1]
	return xk

def exfield_gen(m :int, g):
	''' generates extended field GF(2^m) '''
	n =(1 << m);
	x =(1 << m);
	exp =[0] * (n-1)
	log =[0] * (n)

	for i in range(n -1):
		x = (x >> 1)
		exp[i] = x
		log[x] = i

		if(x & 1):
			x = (x ^ g);
	return exp, log

def poly_add(L :tuple, S :tuple):
	MXLEN =max(len(L), len(S))
	Llen =len(L)-1
	Slen =len(S)-1
	li =[0] * MXLEN

	for i in range(MXLEN):
		if i > Llen:
			li[i] =S[i]
		elif i > Slen:
			li[i] =L[i]
		else:
			li[i] = L[i] + S[i]

	return li

