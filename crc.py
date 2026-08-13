# cyclic redundancy check codes 
import gf
import cir
# import numpy as np 

def encode(n, k, /, u, g, parity =0):
	''' Systematically encode cyclic codes (in binary).
	'''
	codeword =0b0
	taps = g ^ (g & 1)
	lfsr_parameter = (taps, n-k)
	# clock through n _codeword length_
	for clk in range(n):
		u_clk, u =cir.bit_pop(u)

		parity = cir.lfsr(*lfsr_parameter, state =parity, sin =u_clk)
		if(clk < k):
			codeword ^= (u_clk << clk)

	codeword ^= (parity <<k)

	return codeword

def syndrome(n, k, /, r, g, synd =0):
	''' calculate syndrome for cyclic codes. (in binary)
	'''
	synd =0b0	
	taps = g ^ (g & 1)
	lfsr_par = (taps, n-k)
	#clock through n _recieved massage 'r'_
	for clk in range(n):
		r_clk, r =cir.bit_pop(r)

		synd = cir.lfsr(*lfsr_par, state =synd, sin =r_clk)

	return synd


def decode(n, k, /, r, g):
	'''decode or detect error for cyclic codes. (using maggit based structures)
	'''
	# calculate syndrome
	synd = syndrome(n, k, r, g)

	# return r[n-k:] itself if synd ==0
	if synd == 0:
		return r & ((1<<k)-1), synd, True

	# Maggit error correction (shift bits untill 1 error detected)
	# basically xor through all bits and calculate syndrome ...
	# if syndrome == 0 then return the codeword!
	for bit_pos in range(n):
		trial = r ^ (1 << bit_pos)
		if syndrome(n, k, trial, g) == 0:
			return trial & ((1<<k)-1), synd, True

	# If no one-bit candidate closes the syndrome, report the failure contract.
	return r & ((1<<k)-1), synd, False