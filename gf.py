# tools for making finite Galois field:

def XOR(a :bool, b :bool):
	return (a ^ b) 

def AND(a :bool, b :bool):
	return (a and b)

def add(m :int, a, b):
	''' xor in extended field '''
	n = 2**m
	if bool((a | b) >> m):
		a %= n
		b %= n

	return a ^ b

def mul(m :int, a, b, v):
	''' multiplication in extended field '''
	n = 2**m
	if bool((a | b) >> m):
		a %= n
		b %= n
	if (a == 0 | b == 0):
		return 0;
	
	i = v.index(a);
	j = v.index(b);
	xk = v[(i+j) % n];
	return xk

def div(m :int, a, b, v):
	''' division in extended field '''
	n = 2**m
	if bool((a | b) >> m):
		a %= n
		b %= n

	i = v.index(a);
	j = v.index(b);
	xk = v[(i-j) % n];
	return xk

def generator(m :int, p):
	''' function for generating table of power to decimal form'''
	n =(1 << m);
	x =(1 << m);
	v =[0] * (n-1);

	for i in range(n -1):
		x = (x >> 1);
		v[i] = x;

		if(x & 1):
			x = (x ^ p);
	return v
