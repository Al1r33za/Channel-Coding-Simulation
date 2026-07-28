# cyclic redundancy check codes 
import gf
import cir
# import numpy as np 

def encode(n, k, /, u, g, parity =0):
	'''Systematic Cyclic Code encoder.

	INPUTS: 
	---------- 
	(n, k) :(int,int)	/codebook params 
	u :int k bits		/information source 
	g :int n-k+1 bits	/generator polynomial of degree 'n-k' 
	pariy :int n-k bits	/parity check polynomial (initially at rest) 
	----------
	OUTPUTS:
	----------
	codeword :int n bits/codeword polynomial
	'''
	codeword =0b0
	taps = g ^ (g & 1)
	lfsr_par = (taps, n-k)
	# clock through n _codeword length_
	for clk in range(n):
		u_clk, u =cir.bit_pop(u)

		parity = cir.lfsr(*lfsr_par, state =parity, sin =u_clk)
		if(clk < k):
			codeword ^= (u_clk << clk)
	codeword ^= (parity <<k)

	return codeword

def syndrome(n, k, /, r, g, synd =0):
	'''Syndrome polynomial calculation function.

	INPUTS:
	----------
	(n, k) -- codebook params
	r -- received codeword
	g -- generator polynomial of degree 'n-k'
	synd -- syndrome polynomial (initially at rest)
	----------
	OUTPUTS:
	----------
	synd :int n-k bits/syndrome polynomial
	'''
	synd =0b0	
	taps = g ^ (g & 1)
	lfsr_par = (taps, n-k)
	#clock through n _recieved massage 'r'_
	for clk in range(n):
		r_clk, r =cir.bit_pop(r)

		synd = cir.lfsr(*lfsr_par, state =synd, sin =r_clk)

	return synd

def decode():
	pass