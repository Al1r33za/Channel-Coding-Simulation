# cyclic redundancy check codes 
import gf
import numpy as np 

def encode(u, g, k, state =0):
	'''Cyclic code systematic encoder <v(x) = u(x).g(x)> ref:4.5 textbook'''
	v =u;

	for clk in range(k):
		u_bit = (u & 1)
		state = lfsr_clk(u_bit, state, (g >> 1))
		u >>= 1;

	v = (state << k) | v;
	return v

def syndrome_chk(r, g, n, k):
	'''syndrome to check if r(x) codeword or not '''
	state =0
	for clk in range(n):
		state |= ((r&1) << n-k)
		state =yet_another_lfsr(state, g)
		r >>=1
	return state

def decode():
	pass


def lfsr_clk(u_bit, state, taps):
	'''fig 4.1 from text book'''
	gate = u_bit ^ (state & 1)
	if (gate):
		state >>= 1
		state ^= taps
	else:
		state >>= 1

	return state

def yet_another_lfsr(state, taps):
	'''synd lfsr '''
	taps = taps ^ (taps & 1)
	gate = (state & 1)
	if (gate):
		state ^= taps
		state >>=1
	else:
		state >>=1
	return state