# tools for making finite Galois field:
# import time

def mul(a :int, b :int, v :tuple) -> int:
	''' multiply a by b. '''
	m = v[2]
	n = (1 << m)
	if bool((a | b) >> m):
		a %= (n-1)
		b %= (n-1)
	if (a == 0 or b == 0):
		return 0
	
	i =v[1][a]
	j =v[1][b]
	xk = v[0][(i+j) % (n-1)]
	return xk

def div(a :int, b :int, v :tuple) -> int:
	''' divide a by b. '''
	m = v[2]
	n = (1 << m)
	if bool((a | b) >> m):
		a %= (n-1)
		b %= (n-1)
	if (b == 0):
		raise ZeroDivisionError
	if(a == 0):
		return 0

	i =v[1][a]
	j =v[1][b]
	xk = v[0][(i-j) % (n-1)]
	return xk

def power(b :int, p :int, field :tuple) -> int:

	a =field[0]
	e =field[1]
	m =field[2]
	n =(1 << m)-1
	if b == 0:
		return 0 if p>0 else a[0]
	b =e[b]
	return a[(b * p) % n]

def inv(a :int, field :tuple) -> int:
	if a == 0:
		raise ZeroDivisionError
	return power(a, -1, field)

def exfield_gen(m :int, g :int) -> tuple:
	''' generate extended field whit characteristic 2. '''
	n =(1 << m)
	x =(1 << m)
	exp =[0] * (n-1)
	log =[0] * (n)

	for i in range(n -1):
		x = (x >> 1)
		exp[i] = x
		log[x] = i

		if(x & 1):
			x = (x ^ g)
	return exp, log, m, g
