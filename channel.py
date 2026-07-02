# transmitting signal using bpsk modulation through AWGN channel
import numpy as np

def modulation(b :bool, eb =1):
	sm = ((2*eb)**.5)*(1- 2*b);
	return sm

def demodulation(r):
	if (r > 0):
		return 0
	else:
		return 1

def awgn(sm, N0=1):
	n = ((N0/2)**.5)*np.random.randn();
	r = sm + n;
	return r
